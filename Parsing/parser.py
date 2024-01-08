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
            "min_date": 1704450000,

            "max_date": f"{current_timestamp}",
            "offset_peer": {"_": "inputPeerEmpty"},
            "offset_id": 0,
            "limit": 100
        }}
        headers = {"content-type": "application/json"}

        response = requests.get(url, json=payload, headers=headers).json()

        return response
    
    
    def chats(self):
        info = []
        response = self.parsing()
        chats = response['response']['chats']

        for chat in chats:
            pass

        
        return chats

    def messages(self):
        respone = self.parsing()
        messages = respone['response']['messages']

        for message in messages:
            pprint(message)
            text = message['message']
            from_id = message['from_id']
            timestamp = message['date']

