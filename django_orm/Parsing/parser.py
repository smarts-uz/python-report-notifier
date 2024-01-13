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
        url = "http://192.168.3.54:9503/api/messages.searchGlobal"

        payload = {"params": {
            "flags": 0,
            "filter": {"_": "inputMessagesFilterEmpty"},
            "folder_id": None,
            "q": self.q,
            "min_date": datetime.timestamp(self.min_date),
            # "min_date": self.min_date,

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
            username = chat.get('username', 'private chat')
            if username == "private chat":
                public_chat_link = "private chat"
            else:
                public_chat_link = f"https://t.me/{username}"

            data.append({"chat_id": chat_id,
                     "peer_id": peer_id,
                     "title": title,
                     "type": type,
                     "public_chat_link": public_chat_link})

        # with open('db/json/chats.json', mode='w', encoding='utf-8') as file:
        #  json.dump(data, file, indent=4, ensure_ascii=False)

        return data

    def messages(self):

        response = self.parsing()
        messages = response['response']['messages']
        topic_id = None
        data = []
        for message in messages:
            msg_id = message['id']
            text = message['message']
            from_id = message.get('from_id', ' ')
            timestamp = message['date']
            date = datetime.fromtimestamp(timestamp)
            peer_id = message['peer_id']

            user_link = f'tg://user?id={from_id}'
            keyword_id = None
            public_link_chat = None
            private_link_chat = f"https://t.me/c/{int(str(peer_id)[4:])}"
            message_full_link = f"https://t.me/c/{int(str(peer_id)[4:])}/{msg_id}"

            data.append({'user_id': from_id,
                         'datetime': date,
                         'peer_id': peer_id,
                         'content': text,
                         'keyword_id': keyword_id,
                         "private_chat_link": message_full_link,
                         "public_chat_link": public_link_chat,
                         "user_link": user_link})

        return data


    def update_date(self):
        return self.now

#
