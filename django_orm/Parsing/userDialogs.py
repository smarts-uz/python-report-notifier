import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
import django
django.setup()

import requests
from datetime import datetime
import os
from dotenv import load_dotenv

from pprint import pprint


from logx import Logger
save_dialog_to_log = Logger('user_dialog_log', 'a')


ip = os.getenv("IP")
port = os.getenv("PORT")
token = os.getenv("TOKEN")
chat_id = os.getenv("CHAT_ID")

load_dotenv()

# --- Function

# tg_id = 0
# tg_role_id = 0
# type = ''
# full_name = ''
# username = ''

from db.models import TgUser

def user_dialogs():
    url = f"http://192.168.3.54:9503/api/messages.getDialogs"
    response = requests.get(url).json()['response']['users']
    users = []
    try:
        for user in response:
            user_id = user['id']
            is_bot = user['bot']
            first_name = user['first_name']
            username = user.get('username', 'No Username')
            status = user.get('status', {'_': 'No Status'})
            phone = user.get('phone', 'No phone number provided!')
            photo = user.get('photo', {'_': 'noPhoto'})
            mtproto = user

            users.append({
                'tg_id': user_id,
                'bot': is_bot,
                'first_name': first_name,
                'username': username,
                'status': status,
                'phone': phone,
                'photo': photo,
                'mtproto': mtproto
            })
            print(f"Users found: {len(users)}")
            save_dialog_to_log.log(user)
    except Exception as e:
        msg = '[Parser][User]Some kind of error. check log file'
        print(msg)
        save_dialog_to_log.log(msg)
        save_dialog_to_log.err(e)

    # pprint(users)
    # print("---> Users count:", len(users))
    return users


def save_dialogs_to_db():
    users = user_dialogs()
    for user in users:
        try:
            print(f"{user['tg_id']} is Saved to db")
            TgUser.objects.get_or_create(**user)
            save_dialog_to_log.log(f"{user['tg_id']} is Saved to db")
        except Exception as e:
            msg = "Error occured. Check the log file"
            print(msg)
            save_dialog_to_log.log(msg)
            save_dialog_to_log.err(e)

# save_dialogs_to_db()
