import os

import timestamp

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
import django

django.setup()

from db.models import *

import requests
from datetime import datetime
from pprint import pprint

data_channel=[]
data_chat=[]
url = "http://192.168.3.54:9503/api/messages.getDialogs"

response = requests.post(url).json()

for i in response['response']['chats']:
    if i.get('participants_count') is not None:
        if i['_'] =='channel' and i['id'] !=2059626462:
            data_channel.append({
                "type": i['_'],
                "name": i['title'],
                "tg_id":i['id'],
                "participants_count": i['participants_count'],
                "signatures":i['signatures'],
                "created_at" : datetime.fromtimestamp(i['date']),

                                 })

        elif i['id'] !=2059626462 and i['id'] !=4191391621:
            data_chat.append({
                "type": i['_'],
                "name": i['title'],
                "tg_id": i['id'],
                "created_at":datetime.fromtimestamp(i['date']),
                "participants_count": i['participants_count'],
                                            })
    elif i['id'] !=2059626462:
        data_channel.append({
            "type": i['_'],
            "name": (i['title']),
            "tg_id":i['id'],
            "participants_count": None,
            "signatures": i['signatures'],
            "created_at": datetime.fromtimestamp(i['date'])


        })



# for channel in data_channel:
#     print(channel)
#
# for chat in data_chat:
#     print(chat)

try:
    book = TgChannel.objects.get(name=i['title'])

except TgChannel.DoesNotExist:

    for channel_info in data_channel:
        TgChannel.objects.create(**channel_info)

except TgChannel.MultipleObjectsReturned:
    pass




try:
    book = TgGroup.objects.get(name=i['title'])

except TgGroup.DoesNotExist:

    for channel_info in data_channel:
        TgGroup.objects.create(**channel_info)

except TgGroup.MultipleObjectsReturned:
        pass

