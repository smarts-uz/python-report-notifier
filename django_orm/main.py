###########################################################################
## Django ORM Standalone Python Template
############################################################################
""" Here we'll import the parts of Django we need. It's recommended to leave
these settings as is, and skip to START OF APPLICATION section below """

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

from datetime import datetime

now = datetime.now()
#
# # Seed a few users in the database
# Keyword.objects.create(
#     name='#report1',
#     last_checked = now
# )
# Keyword.objects.create(
#     name='#LeftTheOffice2',
#     last_checked = now
# )
# #
# for u in Keyword.objects.all():
#     print(f'ID: {u.id} \tUsername: {u.name}')
#
Users.objects.create(

    fullname='huiaskjn',
    username='supreme',
    user_id=102153213,
)
user = Users.objects.all()


for i in user:

    print(f'ID: {i.id} \tpeer_id: {i.fullname}')




# Message.objects.create(
#
#     name = 'rfiskwo',
#     datetime ='2023-12-16',
#     keyword_id = 1,
#     content = 'text',
#     from_id = 1235857,
#     peer_id = 4324234
# )


#
# for u in Message.objects.all():
#     print(f'ID: {u.id} \tpeer_id: {u.peer_id}')
#
# for u in Chats.objects.all():
#     print(f'ID: {u.id} \ttitle: {u.title}')


from Parsing.parser import Parser

p = Parser()
# users = p.users()
# for user in users:
#     user_id = user['user_id']
#     fullname = user['fullname']
#     username = user['username']
#     Users.objects.create(
#         user_id = user_id,
#         fullname = fullname,
#         username = username
#     )
#     print('success')

#
# Users.objects.create(
#         user_id = 764782,
#         fullname = 'thdj',
#         username = 'hurihq'
#     )

#
# chats = p.chats()
# for chat in chats:
#     chat_id = chat['chat_id']
#     type = chat['type']
#     title = chat['title']
#     Chats.objects.create(
#
#         chat_id=chat_id,
#         type=type,
#         title=title
#
#     )
#     print(f'success id:{chat_id}')
