import requests

import os
from dotenv import load_dotenv

token = os.getenv("TOKEN")
chat_id = os.getenv("CHAT_ID")


class CreateTopic:

    def __init__(self, name):
        self.name = name

    def craeteTopic(self):
        url = f"https://api.telegram.org/bot{token}/createForumTopic"

        payload = {
            "chat_id": f"{chat_id}",
            "name": f"{self.name}",
            "icon_color": "16766590 "
        }

        headers = {"content-type": "application/json"}

        response = requests.post(url, json=payload, headers=headers).json()
        topic_id = response['result']['message_thread_id']

        print(response)
        return topic_id
