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
def channel_dialogs():
    data_channel = []
    data_chat = []

    for chat in response['response']['chats']:
        if chat['_']=='chat' or chat['id']==2059626462:
            continue
        else:
            # If channel
            if chat['megagroup']==False:
                 data_channel.append({
                    "type": 'channel',
                    "name": chat['title'],
                    "tg_id":chat['id'],
                    "signatures":chat['signatures'],
                    "created_at" : datetime.fromtimestamp(chat['date']),
                     "megagroup": chat['megagroup']
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

def saveChannels():
    channels, chats = channel_dialogs()[0], channel_dialogs()[1]
    for channel in channels:
        try:
            TgChannel.objects.get_or_create(**channel)
            msg = f"{channel['name']} is saved!"
            print(msg)
            save_channel_chat_log.log(msg)
        except Exception as e:
            print("Error occured. Check the log file")
            save_channel_chat_log.err(e)

    for chat in chats:
        try:
            TgGroup.objects.get_or_create(**chat)
            msg = f"{chat['name']} is saved!"
            print(msg)
            save_channel_chat_log.log(msg)
        except Exception as e:
            print("Error occured. Check the log file")
            save_channel_chat_log.err(e)

saveChannels()

