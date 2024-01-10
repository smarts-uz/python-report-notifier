############################################################################
## Django ORM Standalone Python Template
############################################################################
""" Here we'll import the parts of Django we need. It's recommended to leave
these settings as is, and skip to START OF APPLICATION section below """
import json
# Turn off bytecode generation
import sys

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

import datetime

now = datetime.datetime.now()
current_timestamp = datetime.datetime.now().astimezone().isoformat()

# for u in Keyword.objects.all():
#     print(f'ID: {u.id} \tUsername: {u.name} \tlast_checked: {u.last_checked}')


# Test py functionality
from Parsing.parser import Parser

p = Parser()

p.users()
p.chats()
p.messages()


def create_users(user_id, username, fullname):
    Users.objects.create(

        user_id=user_id,
        username=username,
        fullname=fullname

    )
    print(f'Users have been saved!: user_id: {user_id} || username: {username} || {fullname}')


def create_chats(chat_id, title, type):
    Chats.objects.create(

        chat_id=chat_id,
        title=title,
        type=type
    )
    print(f'Chats have been saved')


def create_message(datetime, content, from_id, peer):
    Message.objects.create(

        datetime=datetime,
        content=content,
        from_id=from_id,
        peer=peer,

    )

    print('Message have been saved!! ')


with open('db/json/chats.json', mode='r', encoding='utf-8') as file:
    data = json.load(file)
    for chat in data:
        chat_id = chat['chat_id']
        title = chat['title']
        type = chat['type']
        create_chats(chat_id, title, type)

with open('db/json/users.json', mode='r', encoding='utf-8') as file:
    data = json.load(file)
    for user in data:
        user_id = user['user']
        full_name = user['full_name']
        username = user['username']
        create_users(user_id,full_name,username)

with open('db/json/messages.json', mode='r', encoding='utf-8') as file:
    data = json.load(file)
    for i in data:
        print(i)

        time = i['timestamp']
        text = i['text']
        from_id = i['from_id']
        peer_id = i['peer_id']

        create_message(time, text, from_id, peer_id)
