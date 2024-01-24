import requests
from pprint import pprint

data_channel=[]
data_chat=[]
url = "http://192.168.3.54:9503/api/messages.getDialogs"

response = requests.post(url).json()

for i in response['response']['chats']:
    if i.get('participants_count') is not None:
        if i['_'] =='channel':
            data_channel.append({
                "type": i['_'],
                "name": i['title'],
                "tg_id":i['id'],
                "participant_channel": i['participants_count'],
                "signatures":i['signatures'],
                "date" : i['date']
                                 })

        else:
            data_chat.append({
                "type": i['_'],
                "name": i['title'],
                "tg_id": i['id'],
                "date": i['date'],
                "participant_chat": i['participants_count'],
                            })
    else:
        data_channel.append({
            "type": i['_'],
            "name": (i['title']),
            "tg_id":i['id'],
            "participant_channel": None,
            "signatures": i['signatures'],
            "date": i['date']

        })




# print(data_channel)
# print(data_chat)
for channel in data_channel:
    print(channel)
for chat in data_chat:
    print(chat)
