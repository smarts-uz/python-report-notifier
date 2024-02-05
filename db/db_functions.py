import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
import django

django.setup()



from .models import *

from dotenv import load_dotenv
msg_len = os.getenv('MESSAGE_LEN')
load_dotenv()


def all_keywords():
    data = Keyword.objects.values('pk', 'name', 'last_checked', "topic_id")
    return list(data)


def forward_message_boolean(peer_id):
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
    data = TgGroup.objects.values('pk','tg_id','is_active','days_count','name','forum')
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

def get_user_id_form_tg_group_user(user_id):
    channel_id = str(user_id)[4:]
    try:

        user = TgGroupUser.objects.get(tg_group_user_id=user_id)

        from_channel = False
    # except TgGroupUser.DoesNotExist:
    #
    #     user = TgGroupUser.objects.get(tg_group_user_id=channel_id)
    #     from_channel  = False
    except TgGroupUser.DoesNotExist:

        channel = TgChannel.objects.get(tg_id=channel_id)
        from_channel = True
        full_name = channel.name
        try:
            username = channel.username
        except:
            username = None
        user = TgGroupUser.objects.create(
            tg_group_user_id = user_id,
            full_name = full_name,
            username = username
        )






    return user.pk,from_channel


def get_title_from_user_and_message(msg_link:str):
    msg = TgGroupMessage.objects.get(message_private_link=msg_link)
    user_pk = msg.tg_group_user_id

    try:
        user = TgGroupUser.objects.get(pk=user_pk)
        full_name = user.full_name
    except TgGroupUser.DoesNotExist:
        channel = TgChannel.objects.get(pk=user_pk)
        full_name = channel.name
    except:

        full_name = "NotFromUser"


    if len(str(msg.content)) >=50:
        title = f'{full_name}  |  {str(msg.content)[0:int(msg_len)]}'

    else:
        title = f'{full_name}  |  {str(msg.content)[0:int(msg_len)]}'

    return title

def get_thread_id_and_title_from_report():
    report = Report.objects.only("message_link").filter(thread_id=None)
    return report


def get_name_from_keyword():
    keyword = Keyword.objects.only('name').filter(topic_id=None)
    return keyword

def get_username_from_tggroupuser(from_id):
    user = TgGroupUser.objects.get(tg_group_user_id=from_id)
    return user.username

def get_user_id_from_group(peer_id):
    try:
        user = TgGroupUser.objects.get(tg_group_user_id=peer_id)

    except TgGroupUser.DoesNotExist:

        chat_id = int(str(peer_id)[4:])
        gr = TgGroup.objects.get(tg_id=chat_id)
        full_name = gr.name
        username = gr.username
        user = TgGroupUser.objects.create(
            tg_group_user_id=peer_id,
            full_name=full_name,
            username=username
        )
    return user.pk