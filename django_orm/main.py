###########################################################################
## Django ORM Standalone Python Template
############################################################################
""" Here we'll import the parts of Django we need. It's recommended to leave
these settings as is, and skip to START OF APPLICATION section below """

# Turn off bytecode generation
import sys

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


def db_check():
    response = ""
    query = input("Enter query: ")
    response = Keyword.objects.filter(name__icontains=query)
    first_row = response.first()
    if response.exists():
        # print(first_row.last_checked, query)
        return first_row.last_checked, query, first_row.pk
    else:
        new = Keyword.objects.create(
            name=query,
            last_checked=datetime(2010, 1, 1)
        )
        new.save()
        new_row = response.first()

        return new_row.last_checked, query, new_row.pk


instance = db_check()


# print(instance[0])
# print(datetime.timestamp(instance[0]))


# print("Time:", type(instance[0]),"\nQ:", type(instance[1]))

# t = parser.parsing(instance[0], instance[1])


# query = input("Enter query: ")
# response = Keyword.objects.filter(name__icontains=query)
# fm = response.first()
# print(response, fm)

def save_to_db():
    parser = Parser(instance[0], instance[1])
    # Saving chats data to db
    chats = parser.chats()
    for chat in chats:
        print(
            f'Chat has been saved!: chat_id:{chat["chat_id"]}  chat_title:{chat["title"]} public_chat_link: {chat["public_chat_link"]}')
        Chat.objects.get_or_create(**chat)

    # Saving users data to db
    users = parser.users()
    for user in users:
        User.objects.get_or_create(**user)
        print(
            f'User has been saved!: user_id: {user["user_id"]}  fullname : {user["fullname"]} username: {user["username"]}')

    # Saving messages data to db
    messages = parser.messages()
    for message in messages:
        message['keyword_id'] = instance[2]
        user_id = message['user_link']
        content = message['content']
        date = message['datetime']
        private_chat_link = message['private_chat_link']
        message_full_link = message['message_full_link']
        Message.objects.get_or_create(**message)


        print(
            f'Message has been saved!: content: {message["content"]} ,chat_id:  {message["peer_id"]}, user_id: {message["user_id"]}, time: {message["datetime"]} private_chat_link: {message["private_chat_link"]}')
        # print(message)

        send_msg(str(content), user_id, str(private_chat_link), str(date), str(message_full_link))
        print(content,user_id,private_chat_link,date,message_full_link)

    update_time = parser.update_date()
    print("last checked time", update_time)
    key = Keyword.objects.get(name=instance[1])
    key.last_checked = update_time
    key.save()
    print(f'update time is {update_time}')
    print("Successfull end!!!!")

# push
save_to_db()
