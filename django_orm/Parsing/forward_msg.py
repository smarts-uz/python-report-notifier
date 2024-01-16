import requests

from .regFunction import retry_after


class ForwardMsg:

    def __init__(self, peer_id, message_id, topic_id, userlink, date, user_full_name, chat_link, chat_title,
                 message_full_link):
        self.peer_id = peer_id
        self.message_id = message_id
        self.topic_id = topic_id
        self.userlink = userlink
        self.date = date
        self.user_full_name = user_full_name
        self.chat_link = chat_link
        self.chat_title = chat_title
        self.message_full_link = message_full_link

    def forward_message(self):
        url = "https://api.telegram.org/bot6454237457:AAHcoiiJ4gw-Zb9HCbJtHN8HiLkwHlsG474/forwardMessage"

        payload = {
            "chat_id": "-1002059626462",
            "from_chat_id": f"{self.peer_id}",
            "message_id": f"{self.message_id}",
            "message_thread_id": f"{self.topic_id}"
        }
        headers = {"content-type": "application/json"}

        response = requests.post(url, json=payload, headers=headers).json()

        print(f"Message forward : {response['ok']}")
        msg_id = response['result']['message_id']
        while not response['ok']:

            if "Too Many Requests: retry after" in response['description']:
                retry_after(response['description'])
            response = requests.get(url, json=payload, headers=headers).json()
            print(f"Message forward : {response['ok']}")
            if response['ok'] == True:
                break

        return msg_id

    def replyMessage(self):
        url = "https://api.telegram.org/bot6454237457:AAHcoiiJ4gw-Zb9HCbJtHN8HiLkwHlsG474/sendMessage"

        payload = {
            "chat_id": -1002059626462,
            "message_thread_id": self.topic_id,
            "reply_parameters": {
                "message_id": self.forward_message()
            },
            "parse_mode": "HTML",
            "text": f"""
    📅<b>Date</b> : {self.date}
    👤<b>User</b> : <a href="{self.userlink}">{self.user_full_name}</a>
    👥<b>Group/Channel</b> : <a href="{self.chat_link}">{self.chat_title}</a>
    🔗<b>Link</b>: <a href="{self.message_full_link}">Message Link</a>
        """
        }

        headers = {"content-type": "application/json"}

        response = requests.post(url, json=payload, headers=headers).json()
        print(f"Message reply : {response['ok']}")

        while not response['ok']:

            if "Too Many Requests: retry after" in response['description']:
                retry_after(response['description'])
            response = requests.get(url, json=payload, headers=headers).json()
            print(f"Message reply : {response['ok']}")
            if response['ok'] == True:
                break

        return response


