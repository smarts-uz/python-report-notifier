import requests

from .regFunction import retry_after


class CreateTopic:

    def __init__(self, name):
        self.name = name

    def craeteTopic(self):
        url = "https://api.telegram.org/bot6454237457:AAHcoiiJ4gw-Zb9HCbJtHN8HiLkwHlsG474/createForumTopic"

        payload = {
            "chat_id": "-1002059626462",
            "name": f"{self.name}",
            "icon_color": "16766590 "
        }

        headers = {"content-type": "application/json"}

        response = requests.post(url, json=payload, headers=headers).json()
        topic_id = response['result']['message_thread_id']

        print(response)
        return topic_id

    # def get_topic_id(self):
    #     response = self.craeteTopic()
    #
    #     return topic_id


def sendMessage(content, user_link, private_chat_link, date, message_link, user_fullname, chat_title, username,
                topic_id,pk):
    import requests

    url = "https://api.telegram.org/bot6454237457:AAHcoiiJ4gw-Zb9HCbJtHN8HiLkwHlsG474/sendMessage"

    payload = {
        "chat_id": "-1002059626462",
        "text": f"""(PY)<b>№:{pk}</b>
    
📅<b>Date</b> : <u>{date}</u>
👤<b>User</b> :  <a href="t.me/{username}">{user_fullname}</a>
🔗<b>User Link</b> : <tg-spoiler>{user_link}</tg-spoiler>
👥<b>Group/Channel</b> : <a href="{private_chat_link}">{chat_title}</a>
🔗<b>Link</b>: <a href="{message_link}">Message Link</a>

📩<b>Text</b>: <i>{content}</i> """,
        "parse_mode": "HTML",
        "message_thread_id": f"{topic_id}"
    }
    headers = {"content-type": "application/json"}
    response = requests.get(url, json=payload, headers=headers).json()

    print(f"Message send : {response['ok']}")
    while not response['ok']:

        if "Too Many Requests: retry after" in response['description']:
            retry_after(response['description'])
        response = requests.get(url, json=payload, headers=headers).json()
        print(f"Message send : {response['ok']}")
        if response['ok'] == True:
            break



import requests









