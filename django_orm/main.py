###########################################################################
## Django ORM Standalone Python Template
############################################################################
""" Here we'll import the parts of Django we need. It's recommended to leave
these settings as is, and skip to START OF APPLICATION section below """

# Turn off bytecode generation
import sys
import time
from TGBOT.runbot import send_msg, forward_msg

sys.dont_write_bytecode = True

# Django specific settings
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
import django

django.setup()
from db.models import *

from datetime import datetime
from Parsing.parser import Parser

# Import your models for use in your script

############################################################################
## START OF APPLICATION
############################################################################
""" Replace the code below with your own """




def all_keywords():
    data = Keyword.objects.values('pk', 'name', 'last_checked')
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
    return message.pk


def save_to_db():
    print("[Parsing in progress]")
    for item in all_keywords():

        parser = Parser(item['last_checked'], item['name'])

        # Saving chats data to db
        chats = parser.chats()
        for chat in chats:
            print(
                f'[Keyword: {item["name"]}][Chat has been saved]: chat_id:{chat["chat_id"]}  chat_title:{chat["title"]} public_chat_link: {chat["public_chat_link"]}')
            Chat.objects.get_or_create(**chat)

        # Saving users data to db
        users = parser.users()
        for user in users:
            User.objects.get_or_create(**user)
            print(
                f'[Keyword: {item["name"]}][User has been saved]: user_id: {user["user_id"]}  fullname : {user["fullname"]} username: {user["username"]}')

        # Saving messages data to db
        messages = parser.messages()
        for message in messages:
            message['keyword_id'] = item['pk']
            msg_id = message['msg_id_field']
            Message.objects.get_or_create(**message)
            user_link = message['user_link']
            content = message['content']
            date = message['datetime']
            peer_id = message['peer_id']
            private_chat_link = message['private_chat_link']
            message_full_link = message['message_full_link']
            user_id = message['user_id']

            forward_bool = forward_message_boolen(peer_id)
            chat_title = get_title_chat(peer_id)
            user_fullname = get_user_fullname(user_id)[0]
            username = get_user_fullname(user_id)[1]
            pk = get_msg_id(message_full_link)

            print(msg_id)
            print(forward_bool)
            if forward_bool == True:

                print('---')
                send_msg(str(content), user_link, str(private_chat_link), str(date), str(message_full_link),
                         user_fullname, chat_title, pk, username)

            else:
                print(peer_id)
                forward_msg(user_link, user_fullname, chat_title, private_chat_link, str(date), message_full_link,
                            msg_id, peer_id, pk, username)

            print(
                f'[Keyword: {item["name"]}][Message has been saved]: content: {message["content"]} ,chat_id:  {message["peer_id"]}, user_id: {message["user_id"]}, time: {message["datetime"]} private_chat_link: {message["private_chat_link"]}')

            time.sleep(1)

        update_time = parser.update_date()
        print("last checked time", update_time)


        try:
            key = Keyword.objects.get(name=item["name"])
            # Do something with the 'key' object
        except Keyword.DoesNotExist:
            print(f"Keyword with name '{item['name']}' does not exist.")
        key.last_checked = update_time
        key.save()
        print(f'update time is {update_time}')

        for i in range(5):
            print(i + 1)
            time.sleep(1)
        print(f"f[*---------{item['name']}-------------- search successfully ended!! *]")
    print("Successfull end!!!!")


save_to_db()


