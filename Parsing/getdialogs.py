import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
import django
django.setup()

from db.models import *

import requests
from datetime import datetime
from pprint import pprint

from logx import Logger
save_channel_chat_log = Logger('save_channel_chat_log', 'a')

url = "http://192.168.3.54:9503/api/messages.getDialogs"

response = requests.post(url).json()
def get_dialogs():
    data_channel = []
    data_chat = []

    for chat in response['response']['chats']:
        if chat['_']=='chat' or chat['id']==2059626462:
            continue
        else:
            # If channel
            if chat['megagroup']==False:
                if 'username' in chat:
                    data_channel.append({
                        "type": 'channel',
                        "name": chat['title'],
                        "tg_id": chat['id'],
                        "signatures": chat['signatures'],
                        "created_at": datetime.fromtimestamp(chat['date']),
                        "megagroup": chat['megagroup'],
                        "username":chat['username'],
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
                if 'username'in chat :
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


# pprint(channel_dialogs())

def collect_dialogs():
    channels, chats = get_dialogs()[0], get_dialogs()[1]

    for channel in channels:

        try:
           msg= TgChannel.objects.get(tg_id=channel['tg_id'])
           if channel['name']!=msg.name:

               old={f"{datetime.now()}:name":msg.name}
               ext_data=msg.name_history
               if ext_data == None:
                   ext_data = {}


               ext_data.update(old)

               msg.name = channel['name']
               msg.save()

               print(f'[Channel ]name update {channel["name"]}')

           if 'username' in channel:
               if  channel['username']!=msg.username: # For username column in Channel
                   old_username = {f"{datetime.now()}:username": msg.username}
                   ext_data_username = msg.username_history


                   ext_data_username.update(old_username)

                   msg.username = channel['username']
                   msg.save()

                   print(f'[Channel ]username update {channel["username"]}')


        except TgChannel.DoesNotExist:
            TgChannel.objects.create(**channel)
            msg = f"{channel['name']} is saved!"
            print(msg)
            save_channel_chat_log.log(msg)
        except Exception as e:
            print("Error occured. Check the log file")
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

                print(f'Chat name update {chat["name"]}')

            if 'username' in chat:
                if chat['username'] != msg.username:  # For username column in Chat

                    old_username = {f"{datetime.now()}:username": msg.username}
                    ext_data_username = msg.username_history

                    ext_data_username.update(old_username)

                    msg.username = chat['username']
                    msg.save()

                    print(f'Chat username update {chat["username"]}')
        except TgGroup.DoesNotExist:
            TgGroup.objects.create(**chat)
            msg = f"{chat['name']} is saved!"
            print(msg)
            save_channel_chat_log.log(msg)
        except Exception as e:
            print("Error occured. Check the log file")
            save_channel_chat_log.err(e)


