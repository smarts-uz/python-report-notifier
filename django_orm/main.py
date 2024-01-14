###########################################################################
## Django ORM Standalone Python Template
############################################################################
""" Here we'll import the parts of Django we need. It's recommended to leave
these settings as is, and skip to START OF APPLICATION section below """

# Turn off bytecode generation
import sys
import time
from telegram_bot.runbot import send_msg

sys.dont_write_bytecode = True

# Django specific settings
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
import django

django.setup()

# Import your models for use in your script
from db.models import *

############################################################################
## START OF APPLICATION
############################################################################
""" Replace the code below with your own """

from datetime import datetime
from Parsing.parser import Parser


# -----search by query----

# def db_check():
#     response = ""
#     query = input("Enter query: ")
#     response = Keyword.objects.filter(name__icontains=query)
#     first_row = response.first()
#     if response.exists():
#         # print(first_row.last_checked, query)
#         return first_row.last_checked, query, first_row.pk
#     else:
#         new = Keyword.objects.create(
#             name=query,
#             last_checked=datetime(2010, 1, 1)
#         )
#         new.save()
#         new_row = response.first()
#
#         return new_row.last_checked, query, new_row.pk


# instance = db_check()

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
    return user.fullname



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
            user_link = message['user_link']
            content = message['content']
            date = message['datetime']
            peer_id = message['peer_id']
            private_chat_link = message['private_chat_link']
            message_full_link = message['message_full_link']
            user_id = message['user_id']
            Message.objects.get_or_create(**message)
            forward_bool = forward_message_boolen(peer_id)
            chat_title = get_title_chat(peer_id)
            user_fullname = get_user_fullname(user_id)

            print(msg_id)
            print(forward_bool)
            if forward_bool == True:
                print('---')
                send_msg(str(content), user_link, str(private_chat_link), str(date), str(message_full_link),user_fullname,chat_title)
            else:
                print(peer_id)
                # forward_msg(user_id,private_chat_link,str(date),message_full_link,msg_id,peer_id)

            print(
                f'[Keyword: {item["name"]}][Message has been saved]: content: {message["content"]} ,chat_id:  {message["peer_id"]}, user_id: {message["user_id"]}, time: {message["datetime"]} private_chat_link: {message["private_chat_link"]}')
            # print(message)

            time.sleep(2)
            print(content, user_id, private_chat_link, date, message_full_link)

        # update_time = parser.update_date()
        # print("last checked time", update_time)
        # key = Keyword.objects.get(name=item[1])
        # key.last_checked = update_time
        # key.save()
        # print(f'update time is {update_time}')

        for i in range(5):
            print(i + 1)
            time.sleep(1)
        print(f"f[*---------{item['name']}-------------- search successfully ended!! *]")
    print("Successfull end!!!!")


save_to_db()
