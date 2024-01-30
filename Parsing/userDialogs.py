import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
import django
django.setup()

import requests
from datetime import datetime
import os
from dotenv import load_dotenv
load_dotenv()
from pprint import pprint


from logx import Logger
save_dialog_to_log = Logger('user_dialog_log', 'a')


ip = os.getenv("IP")
port = os.getenv("PORT")
token = os.getenv("TOKEN")
chat_id = os.getenv("CHAT_ID")


# --- Function

# tg_id = 0
# tg_role_id = 0
# type = ''
# full_name = ''
# username = ''

from db.models import TgUser

def user_dialogs():
    url = f"http://{ip}:{port}/api/messages.getDialogs"
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
            try:
                usr = TgUser.objects.get(tg_id=user['tg_id'])
                if user['first_name'] != usr.first_name:
                    count = usr.old_first_name_count + 1
                    old_name = {f"{count}:first_name": usr.first_name}
                    ext_name = usr.old_first_name
                    ext_name.update(old_name)
                    usr.first_name = user['first_name']
                    usr.old_first_name_count = count
                    usr.save()
                    print(f'[User][first_name] updated {user["tg_id"]}')
                    save_dialog_to_log.log(f"[User][UPDATED FIRSTNAME]{user}")

                if user['username'] != usr.username:
                    count = usr.old_username_count + 1
                    old_user = {f"{count}:username": usr.username}
                    ext_username = usr.old_username
                    ext_username.update(old_user)
                    usr.username = user['username']
                    usr.old_username_count = count
                    usr.save()
                    print(f'[Group][user][username] updated {user["tg_group_user_id"]}')
                    save_dialog_to_log.log(f"[User][UPDATED USERNAME]{user}")
                if user['phone'] != usr.phone:
                    count = usr.old_phone_count + 1
                    old_phones = {f"{count}:phone": usr.phone}
                    ext_phone = usr.old_phone
                    ext_phone.update(old_phones)
                    usr.phone = user['phone']
                    usr.old_phone_count = count
                    usr.save()
                    print(f'[Group][user][phone] updated {user["tg_group_user_id"]}')
                    save_dialog_to_log.log(f"[User][UPDATED PHONE]{user}")
                else:
                    print('[Group]user already exist')
                    save_dialog_to_log.log(f"[Group][NOTHING UPDATE]: {user}")


            except TgUser.DoesNotExist:
                TgUser.objects.create(**user)
                print(f'[Group][User has been saved to db] user_id :  {user["tg_id"]}')
                save_dialog_to_log.log(f"[Group][User has been saved to db] {user}")
        except Exception as e:
            print('[Group][User][Some Kind of error check the log file]')
            save_dialog_to_log.err(f'[Group][User error]: {e}')
    print(f'[User] : saving to db successfully end!')
    save_dialog_to_log.log(f'[User] : saving to db successfully end!')



