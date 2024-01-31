# ORM functionality
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
import django
django.setup()

# .env functionality
from dotenv import load_dotenv
load_dotenv()

# Other packages
import requests
from pprint import pprint

# ORM imports


# Logger functionality
from logx import Logger
log_file_name = 'get_forum_topic_log'
save_dialog_to_log = Logger(log_file_name, 'a')

# Receive .env data
ip = os.getenv("IP")
port = os.getenv("PORT")
token = os.getenv("TOKEN")
chat_id = os.getenv("CHAT_ID")
chat_id_2 = os.getenv("CHAT_ID_2")


def check_topics(peer_id):
    data = []
    url = f"http://{ip}:{port}/api/channels.getForumTopics"
    payload = {
        "data": {
            "flags": 0,
            "channel": peer_id
        }
    }
    headers = {"content-type": "application/json"}

    response = requests.get(url, json=payload, headers=headers).json()

    for topic in response['response']['topics']:
        title = topic['title']
        thread_id = topic['id']
        data.append({
            'thread_id':thread_id,
            'thread_title' : title
        })

    return data


