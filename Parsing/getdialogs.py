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
save_channel_chat_log = Logger(log_file_name, 'a',subdirectory='parsing')

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
        username = None
        participants_count=None
        admin_rights = None
        default_banned_rights = None
        noforwards=None

        try:
            username = chat['username']

        except:
            username = None
        try:
            admin_rights = chat['admin_rights']
        except:
            admin_rights = None

        try:
            default_banned_rights = chat['default_banned_rights']
        except:
            default_banned_rights = None
        try:
            noforwards=chat['noforwards']
        except:
            noforwards=None

        try:
            participants_count=chat['participants_count']
        except:
            participants_count=0

        if chat['_']=='chat' or chat['id'] == group_peer_id or chat['id'] == group_peer_id_2:
            continue
        elif chat['megagroup'] == False:
            data_channel.append({
                "type": 'channel',
                "name": chat['title'],
                "tg_id": chat['id'],
                "signatures": chat['signatures'],
                "participants_count": participants_count,
                "created_at": datetime.fromtimestamp(chat['date']),
                "megagroup": chat['megagroup'],
                "username": username,
                "noforwards": noforwards,
                "creator": chat['creator'],
                "broadcast": chat['broadcast'],
                "verified": chat['verified'],
                "restricted": chat['restricted'],
                "min": chat['min'],
                "slowmode_enabled": chat['slowmode_enabled'],
                "scam": chat['scam'],
                "has_link": chat['has_link'],
                "has_geo": chat['has_geo'],
                "photo": chat['photo'],
                "call_active": chat['call_active'],
                "call_not_empty": chat['call_not_empty'],
                "fake": chat['fake'],
                "gigagroup": chat['gigagroup'],
                "join_to_send": chat['join_to_send'],
                "join_request": chat['join_request'],
                "forum": chat['forum'],
                "stories_hidden": chat['stories_hidden'],
                "stories_hidden_min": chat['stories_hidden_min'],
                "stories_unavailable": chat['stories_unavailable'],
                "admin_rights": admin_rights,
                "default_banned_rights": default_banned_rights,
            })
        elif chat['megagroup'] == True:
            data_chat.append({
                "type": 'chat',
                "name": chat['title'],
                "tg_id": chat['id'],
                "created_at": datetime.fromtimestamp(chat['date']),
                "participants_count": participants_count,
                "megagroup": chat['megagroup'],
                "username": username,
                "noforwards":noforwards,
                 "creator": chat['creator'],
                "broadcast": chat['broadcast'],
                "verified": chat['verified'],
                "restricted": chat['restricted'],
                "signatures": chat['signatures'],
                "min": chat['min'],
                "scam": chat['scam'],
                "has_link": chat['has_link'],
                "has_geo": chat['has_geo'],
                "call_active": chat['call_active'],
                "call_not_empty": chat['call_not_empty'],
                "fake": chat['fake'],
                "slowmode_enabled":chat['slowmode_enabled'],
                "gigagroup": chat['gigagroup'],
                "join_to_send": chat['join_to_send'],
                "join_request": chat['join_request'],
                "forum": chat['forum'],
                "photo" :chat['photo'],
                "stories_hidden": chat['stories_hidden'],
                "stories_hidden_min": chat['stories_hidden_min'],
                "stories_unavailable": chat['stories_unavailable'],
                "admin_rights": admin_rights,
                "default_banned_rights": default_banned_rights,

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
                if msg.name_history == None:
                    msg.name_history = {}
                msg.name_history.update(old)

                msg.name = channel['name']
                msg.save()
                print(f'Channel name {old} has been updated to {channel["name"]}')
                save_channel_chat_log.log(f'Channel name {old} has been updated to {channel["name"]}')

            if 'username' in channel:
                if  channel['username'] != msg.username: # For username column in Channel
                    old_username = {f"{datetime.now()}:username": msg.username}
                    if msg.username_history ==None:
                        msg.username_history={}
                    msg.username_history.update(old_username)

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
                if msg.name_history ==None:
                    msg.name_history={}

                msg.name_history.update(old)

                msg.name = chat['name']
                msg.save()
                print(f'Chat name {old} has been updated to {chat["name"]}!')
                save_channel_chat_log.log(f'Chat name {old} has been updated to {chat["name"]}!')

            if 'username' in chat:
                if chat['username'] != msg.username:  # For username column in Chat
                    old_username = {f"{datetime.now()}:username": msg.username}
                    if msg.username_history==None:
                        msg.username_history={}

                    msg.username_history.update(old_username)

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
