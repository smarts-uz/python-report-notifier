import requests
from datetime import datetime

from logx import Logger

parser_log = 'parser_log'
save_parser_to_log = Logger(f'{parser_log}', 'a')
import os
from dotenv import load_dotenv
load_dotenv()


IP = os.getenv("IP")
PORT = os.getenv("PORT")
group_id = os.getenv("CHAT_ID")  # example -1002059626462
group_peer_id = str(group_id)[4:]  # example 2059626462
group_id_2 = os.getenv('CHAT_ID_2')  # example -1002059626462
group_peer_id_2 = str(group_id_2)[4:]  # example 2059626462


class Parser:
    now = datetime.now()
    current_timestamp = datetime.timestamp(now)

    def __init__(self, min_date, q):
        self.min_date = min_date
        self.q = q

    def parsing(self):
        # url = f"http://{ip}:{port}/api/messages.searchGlobal"
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
        try:
            response = requests.get(url, json=payload, headers=headers).json()
            msg = "Parsing is starting"
            save_parser_to_log.log(msg)

        except Exception as e:
            msg = f'<!> Oops! Something went wrong, check the log file: {parser_log}.log'
            print(msg)
            save_parser_to_log.err(e)

        return response

    def users(self):
        data = []
        try:
            response = self.parsing()
            users = response['response']['users']
            for user in users:
                user_id = user.get("id", "This is not user")
                if user == [136817688, 211246197]:
                    continue

                fullname = f'{user.get("first_name", " ")} {user.get("last_name", " ")}'
                username = user.get('username', ' ')

                data.append({'user_id': user_id,
                             'fullname': fullname,
                             'username': username})
                save_parser_to_log.log(user)
        except Exception as e:
            msg = f'<!> Oops! Something went wrong, check the log file: {parser_log}.log'
            print(msg)
            save_parser_to_log.err(e)

        # with open('db/json/users.json', mode='w', encoding='utf-8') as file:
        #  json.dump(data, file, indent=4, ensure_ascii=False)

        return data

    def chats(self):
        data = []
        try:
            response = self.parsing()
            chats = response['response']['chats']

            for chat in chats:

                if chat['id'] == int(group_peer_id) or chat['id'] == int(group_peer_id_2):  # 2059626462

                    continue

                chat_id = chat['id']

                peer_id = int("-100" + str(chat_id))
                title = chat['title']
                type = chat['_']
                forward_message = chat['noforwards']
                username = chat.get('username', 'private chat')
                if username == "private chat":
                    public_chat_link = "private chat"
                else:
                    public_chat_link = f"t.me/{username}"

                data.append({"chat_id": chat_id,
                             "peer_id": peer_id,
                             "title": title,
                             "type": type,
                             "public_chat_link": public_chat_link,
                             "forward_message": forward_message})
                save_parser_to_log.log(chat)
        except Exception as e:
            msg = f'<!> Oops! Something went wrong, check the log file: {parser_log}.log'
            print(msg)

            save_parser_to_log.err(e)

        return data

    def messages(self):
        data = []
        try:
            response = self.parsing()
            messages = response['response']['messages']
            topic_id = None

            for message in messages:

                # content group

                if message['peer_id'] == int(group_id) or message['peer_id'] == int(group_id_2):  # example-1002059626462

                    continue
                peer_id = message['peer_id']



                msg_id = message['id']
                text = message.get("message", " ")
                from_id = message.get('from_id', ' ')
                timestamp = message['date']
                date = datetime.fromtimestamp(timestamp)

                user_link = f'tg://user?id={from_id}'
                keyword_id = None
                public_link_chat = None
                private_link_chat = f"t.me/c/{int(str(peer_id)[4:])}"
                message_full_link = f"t.me/c/{int(str(peer_id)[4:])}/{msg_id}"

                data.append({'user_id': from_id,
                             'datetime': date,
                             'peer_id': peer_id,
                             'content': text,
                             'keyword_id': keyword_id,
                             "private_chat_link": private_link_chat,
                             "message_full_link": message_full_link,
                             "public_chat_link": public_link_chat,
                             "user_link": user_link,
                             "msg_id": msg_id
                             })
                save_parser_to_log.log(message)
        except Exception as e:
            msg = f'<!> Oops! Something went wrong, check the log file: {parser_log}.log'
            print(msg)

            save_parser_to_log.err(e)

        return data

    def update_date(self):
        return self.now
