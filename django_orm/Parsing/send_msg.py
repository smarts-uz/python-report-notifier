import requests

import os
from dotenv import load_dotenv

from regexF.regexFunction import retry_after

token = os.getenv("TOKEN")
chat_id = os.getenv("CHAT_ID")

load_dotenv()


def sendMessage(content, user_link, private_chat_link, date, message_link, user_fullname, chat_title, username,
                topic_id, pk):
    url = f"https://api.telegram.org/bot6454237457:AAHcoiiJ4gw-Zb9HCbJtHN8HiLkwHlsG474/sendMessage"

    payload = {
        "chat_id": f"-1002059626462",
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
        print(response)

        if "Too Many Requests: retry after" in response['description']:
            retry_after(response['description'])
        response = requests.get(url, json=payload, headers=headers).json()
        print(f"Message send : {response['ok']}")
        if response['ok'] == True:
            break
