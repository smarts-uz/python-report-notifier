import requests
from pprint import pprint
from datetime import datetime

now = datetime.now()
current_timestamp = datetime.timestamp(now)


class Parser:
    def __init__(self):
        pass

    def parsing(self):
        url = "http://192.168.3.54:9503/api/messages.searchGlobal"

        payload = {"params": {
            "flags": 0,
            "filter": {"_": "inputMessagesFilterEmpty"},
            "folder_id": None,
            "q": "#report",
            "min_date": 1720129,

            "max_date": f"{current_timestamp}",
            "offset_peer": {"_": "inputPeerEmpty"},
            "offset_id": 0,
            "limit": 100
        }}
        headers = {"content-type": "application/json"}

        response = requests.get(url, json=payload, headers=headers).json()

        return response

    def users(self):
        response = self.parsing()
        users = response['response']['users']
        for user in users:
            user_id = user['id']
            fullname = f'{user.get("first_name"," ")} {user.get("last_name"," ")}'
            username = user.get('username',' ')
            # print(f"{user_id}"
            #       f"{fullname}"
            #       f"{username}"
            #       )


    def chats(self):

        response = self.parsing()
        chats = response['response']['chats']

        for chat in chats:
            # print(chat)
            chat_id = chat['id']
            title = chat['title']
            type = chat['_']





    def messages(self):
        response = self.parsing()
        messages = response['response']['messages']
        topic_id = None
        for message in messages:

            text = message['message']
            from_id = message.get('from_id', ' ')
            timestamp = message['date']
            peer_id = message['peer_id']
            # if message.get('reply_to',' ') is not ' ':
            #     topic_id = message['reply_to']['reply_to_msg_id']


#             print(f"""
#             {text}
# {from_id}
# {timestamp}
# {peer_id}
# {topic_id}""")
