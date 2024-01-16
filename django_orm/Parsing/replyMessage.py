import requests
# from ..main import all_keywords

# message_id = 373

def replyMessage(message_id, topic_id, date, user_full_name, userlink, chat_title, chat_link, message_full_link):
    url = "https://api.telegram.org/bot6454237457:AAHcoiiJ4gw-Zb9HCbJtHN8HiLkwHlsG474/sendMessage"

    payload = {
            "chat_id": -1002059626462,
            "message_thread_id": topic_id,
            "reply_parameters": {
                "message_id":message_id
                },
            "parse_mode": "HTML",
            "text": f"""
📅<b>Date</b> : {date}
👤<b>User</b> : <a href="{userlink}">{user_full_name}</a>
👥<b>Group/Channel</b> : <a href="{chat_link}">{chat_title}</a>
🔗<b>Link</b>: <a href="{message_full_link}">Message Link</a>
    """
        }


    headers = {"content-type": "application/json"}

    response = requests.post(url, json=payload, headers=headers).json()
    print(response)
    return response

replyMessage(290, 372, "Jan 16", "Jon Doe", "@johndoe", "Hello Chat", "@hellochat", "https://t.me/c/2059626462/1/290")