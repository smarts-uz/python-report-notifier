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
from datetime import datetime
from pprint import pprint

# ORM imports
from db.models import *

# Logger
from logx import Logger
log_file_name = 'save_channel_chat_log'
save_channel_chat_log = Logger(log_file_name, 'a')

# Receive .env data
ip = os.getenv("IP")
port = os.getenv("PORT")
group_id = os.getenv("CHAT_ID") #example -1002059626462
group_peer_id = int(str(group_id)[4:]) #example 2059626462
group_id_2 = os.getenv('CHAT_ID_2') #example -1002059626462
group_peer_id_2 = int(str(group_id_2)[4:]) #example 2059626462


def get_dialogs():
    url = f"http://{ip}:{port}/api/messages.getDialogs"
    response = requests.get(url).json()
    data_channel = []
    data_chat = []
    for chat in response['response']['chats']:
        if chat['_']=='chat' or chat['id']==group_peer_id or chat['id'] ==group_peer_id_2 :
            continue
        else:
            # If channel
            if chat['megagroup'] == False:
                if 'username' in chat:
                    data_channel.append({
                        "type": 'channel',
                        "name": chat['title'],
                        "tg_id": chat['id'],
                        "signatures": chat['signatures'],
                        "created_at": datetime.fromtimestamp(chat['date']),
                        "megagroup": chat['megagroup'],
                        "username": chat['username'],
                        })
                else:
                     data_channel.append({
                        "type": 'channel',
                        "name": chat['title'],
                        "tg_id":chat['id'],
                        "signatures":chat['signatures'],
                        "created_at" : datetime.fromtimestamp(chat['date']),
                         "megagroup": chat['megagroup']
                    })
            else:
                if 'username' in chat:
                    data_chat.append({
                        "type": 'chat',
                        "name": chat['title'],
                        "tg_id": chat['id'],
                        "created_at": datetime.fromtimestamp(chat['date']),
                        "participants_count": chat['participants_count'],
                        "megagroup": chat['megagroup'],
                        "username": chat['username'],
                    })
                else:
                    data_chat.append({
                        "type": 'chat',
                        "name": chat['title'],
                        "tg_id": chat['id'],
                        "created_at": datetime.fromtimestamp(chat['date']),
                        "participants_count": chat['participants_count'],
                        "megagroup": chat['megagroup']
                    })
    return data_channel, data_chat


def collect_dialogs():
    channels, chats = get_dialogs()[0], get_dialogs()[1]

    for channel in channels:
        try:
            # Check for channel if it is available in DB. If so, change its name
            msg = TgChannel.objects.get(tg_id=channel['tg_id'])
            if channel['name'] != msg.name:
                old = {f"{datetime.now()}:name":msg.name}
                ext_data = msg.name_history
                if ext_data == None:
                    ext_data = {}
                ext_data.update(old)

                msg.name = channel['name']
                msg.save()
                print(f'Channel name {old} has been updated to {channel["name"]}')
                save_channel_chat_log.log(f'Channel name {old} has been updated to {channel["name"]}')

            if 'username' in channel:
                if  channel['username'] != msg.username: # For username column in Channel
                    old_username = {f"{datetime.now()}:username": msg.username}
                    ext_data_username = msg.username_history
                    ext_data_username.update(old_username)

                    msg.username = channel['username']
                    msg.save()
                    print(f'Channel username {old_username} has been updated to {channel["username"]}!')
                    save_channel_chat_log.log(f'Channel username {old_username} has been updated to {channel["username"]}!')

        except TgChannel.DoesNotExist:
            TgChannel.objects.create(**channel)
            msg = f"New channel with name {channel['name']} has been created on DB!"
            print(msg)
            save_channel_chat_log.log(msg)
        except Exception as e:
            print(f"<!> Oops! Something went wrong, check the log file: {log_file_name}.log")
            save_channel_chat_log.err(e)

    for chat in chats:
        try:
            msg = TgGroup.objects.get(tg_id=chat['tg_id'])
            if chat['name'] != msg.name:
                old = {f"{datetime.now()}:name": msg.name}
                ext_data = msg.name_history
                ext_data.update(old)

                msg.name = chat['name']
                msg.save()
                print(f'Chat name {old} has been updated to {chat["name"]}!')
                save_channel_chat_log.log(f'Chat name {old} has been updated to {chat["name"]}!')

            if 'username' in chat:
                if chat['username'] != msg.username:  # For username column in Chat
                    old_username = {f"{datetime.now()}:username": msg.username}
                    ext_data_username = msg.username_history
                    ext_data_username.update(old_username)

                    msg.username = chat['username']
                    msg.save()
                    print(f'Chat username {old_username} has been updated to {chat["username"]}!')
                    save_channel_chat_log.log(f'Chat username {old_username} has been updated to {chat["username"]}!')
        except TgGroup.DoesNotExist:
            TgGroup.objects.create(**chat)
            msg = f"New chat with name {chat['name']} has been created on DB!"
            print(msg)
            save_channel_chat_log.log(msg)
        except Exception as e:
            print("<!> Oops! Something went wrong, check the log file: {log_file_name}.log")
            save_channel_chat_log.err(e)