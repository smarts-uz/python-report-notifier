import requests
from pprint import pprint
from datetime import datetime
import json




class Parser:
    now = datetime.now()
    current_timestamp = datetime.timestamp(now)


    def __init__(self, min_date, q):
        self.min_date = min_date
        self.q = q

    def parsing(self):
        url = "http://192.168.1.209:9503/api/messages.searchGlobal"

        payload = {"params": {
            "flags": 0,
            "filter": {"_": "inputMessagesFilterEmpty"},
            "folder_id": None,
            "q": self.q,
            # "min_date": datetime.timestamp(self.min_date),
            "min_date": self.min_date,

            "max_date": f"{self.current_timestamp}",
            "offset_peer": {"_": "inputPeerEmpty"},
            "offset_id": 0,
            "limit": 100
        }}
        headers = {"content-type": "application/json"}

        response = requests.get(url, json=payload, headers=headers).json()

        print(self.q, self.min_date)

        return response

    def users(self):
        data = []
        response = self.parsing()
        users = response['response']['users']
        for user in users:
            user_id = user['id']
            fullname = f'{user.get("first_name", " ")} {user.get("last_name", " ")}'
            username = user.get('username', ' ')
            # print(f"{user_id}"
            #       f"{fullname}"
            #       f"{username}"
            #       )
            data.append({'user_id': user_id,
                         'fullname': fullname,
                         'username': username})
        # with open('db/json/users.json', mode='w', encoding='utf-8') as file:
        #  json.dump(data, file, indent=4, ensure_ascii=False)

        return data

    def chats(self):
        data = []
        response = self.parsing()
        chats = response['response']['chats']

        for chat in chats:
            # print(chat)
            chat_id = chat['id']
            peer_id = int("-100" + str(chat_id))
            title = chat['title']
            type = chat['_']

            data.append({"chat_id": chat_id,
                         "peer_id": peer_id,
                         "title": title,
                         "type": type})
        # with open('db/json/chats.json', mode='w', encoding='utf-8') as file:
        #  json.dump(data, file, indent=4, ensure_ascii=False)


        return data

    def messages(self):
        response = self.parsing()
        messages = response['response']['messages']
        topic_id = None
        data = []
        for message in messages:
            text = message['message']
            from_id = message.get('from_id', ' ')
            timestamp = message['date']
            date = datetime.fromtimestamp(timestamp)
            peer_id = message['peer_id']
            keyword_id = None

            data.append({'user_id': from_id,
                         'datetime': date,
                         'peer_id': peer_id,
                         'content': text,
                         'keyword_id': keyword_id})

        return data

    def update_date(self):
        return self.now
# #
# p = Parser(1610376471, "#report")
# a = p.update_date()
# # print(a)
# print(p.chats())