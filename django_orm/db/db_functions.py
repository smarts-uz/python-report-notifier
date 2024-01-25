import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
import django

django.setup()

from .models import *

def all_keywords():
    data = Keyword.objects.values('pk', 'name', 'last_checked', "topic_id")
    return list(data)


def forward_message_boolen(peer_id):
    chat = Chat.objects.get(peer_id=peer_id)
    return chat.forward_message


def get_title_chat(peer_id):
    chat = Chat.objects.get(peer_id=peer_id)
    return chat.title


def get_user_fullname(user_id):
    user = User.objects.get(user_id=user_id)
    return user.fullname, user.username


def get_msg_id(msg_full_link):
    message = Message.objects.get(message_full_link=msg_full_link)
    return message.first.pk



def get_all_group():
    data = TgGroup.objects.values('pk','tg_id','is_active','days_count')
    return list(data)
