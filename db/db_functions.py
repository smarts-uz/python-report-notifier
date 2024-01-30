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
    data = TgGroup.objects.values('pk','tg_id','is_active','days_count','name')
    return list(data)

def get_all_channel():
    data = TgChannel.objects.values('pk','tg_id','is_active','days_count','name')
    return list(data)


def get_message_from_group(msg_link):
    msg = TgGroupMessage.objects.get(message_private_link = msg_link)
    return (msg.pk,
            msg.msg_id,
            msg.peer_id,
            msg.topic_id,
            msg.replies_count)

def get_reply_messages(reply_msg_id):
    msg = TgGroupMessage.objects.all().filter(reply_to_msg_id=reply_msg_id)

    return msg

def get_all_reports():
    data = Report.objects.values('pk','message_id', 'message_link','thread_id')
    return list(data)

def get_forward(peer_id):
    chat_id = int(str(peer_id)[4:])
    data = TgGroup.objects.get(tg_id=chat_id)
    return data.noforwards


def get_fullname_from_rating(user_id):
    user = TgGroupUser.objects.get(tg_group_user_id=user_id)
    return user.full_name

def get_title_from_collect_group(chat_id):
    chat = TgGroup.objects.get(tg_id=chat_id)
    return chat.name



