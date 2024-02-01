# ORM functionality
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
import django
django.setup()

# .env functionality
from dotenv import load_dotenv
load_dotenv()

# Other packages
import requests

# ORM imports
from db.models import TgUser

# Logger functionality
from logx import Logger
log_file_name = 'user_dialog_log'
save_dialog_to_log = Logger(log_file_name, 'a')

# Receive .env data
ip = os.getenv("IP")
port = os.getenv("PORT")
token = os.getenv("TOKEN")
chat_id = os.getenv("CHAT_ID")


# --- Main Functions
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
            save_dialog_to_log.log(user)
        print(f"Total users found: {len(users)}")
    except Exception as e:
        msg = f"<!> Oops! Something went wrong, check the log file: {log_file_name}.log"
        print(msg)
        save_dialog_to_log.log(msg)
        save_dialog_to_log.err(e)
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
                    print(f"User with ID {user['tg_id']} updated <first_name> to: {user['first_name']}")
                    save_dialog_to_log.log(f"User with ID {user['tg_id']} updated <first_name> to: {user['first_name']}")

                if user['username'] != usr.username:
                    count = usr.old_username_count + 1
                    old_user = {f"{count}:username": usr.username}
                    ext_username = usr.old_username
                    ext_username.update(old_user)
                    usr.username = user['username']
                    usr.old_username_count = count
                    usr.save()
                    print(f"User with ID {user['tg_id']} updated <username> to: {user['username']}")
                    save_dialog_to_log.log(f"User with ID {user['tg_id']} updated <username> to: {user['username']}")
                if user['phone'] != usr.phone:
                    count = usr.old_phone_count + 1
                    old_phones = {f"{count}:phone": usr.phone}
                    ext_phone = usr.old_phone
                    ext_phone.update(old_phones)
                    usr.phone = user['phone']
                    usr.old_phone_count = count
                    usr.save()
                    print(f"User with ID {user['tg_id']} updated <phone> to: {user['phone']}")
                    save_dialog_to_log.log(f"User with ID {user['tg_id']} updated <phone> to: {user['phone']}")
                else:
                    print(f"User with ID {user['tg_id']} already exist")
                    save_dialog_to_log.log(f"User with ID {user['tg_id']} already exist.")


            except TgUser.DoesNotExist:
                TgUser.objects.create(**user)
                print(f"User with ID {user['tg_id']} has been saved to DB.")
                save_dialog_to_log.log(f"User with ID {user['tg_id']} has been saved to DB.")
        except Exception as e:
            print(f"<!> Oops! Something went wrong, check the log file: {log_file_name}.log")
            save_dialog_to_log.err(e)
    print(f"DB save process has been finished!")
    save_dialog_to_log.log(f"DB save process has been finished!")


"<!> Oops! Something went wrong, check the log file: "