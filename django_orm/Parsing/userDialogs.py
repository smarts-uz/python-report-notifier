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
            mtproto = 0 # have not yet decided

            users.append({
                'user_id': user_id,
                'bot': is_bot,
                'first_name': first_name,
                'username': username,
                'status': status,
                'phone': phone,
                'photo': photo
            })
            save_dialog_to_log.log(user)
    except Exception as e:
        msg = '[Parser][User]Some kind of error. check log file'
        print(msg)
        save_dialog_to_log.log(msg)
        save_dialog_to_log.err(e)

    pprint(users)
    print("---> Users count:", len(users))
    return users


user_dialogs()