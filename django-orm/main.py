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

# Seed a few users in the database
Keyword.objects.create(
    name='#report1',
    last_checked = now
)
Keyword.objects.create(
    name='#LeftTheOffice2',
    last_checked = now
)
#
for u in Keyword.objects.all():
    print(f'ID: {u.id} \tUsername: {u.name}')
#
# Users.objects.create(
#     user_id = 32153213,
#     username = 'supreme',
#     fullname = 'huiaskjn',
# )

Chats.objects.create(
    id = 11,
    chat_id = 2124633,
    type = 'chats',
    title = 'parser'

)
#
# for u in Users.objects.all():
#     print(f'ID: {u.id} \tUsername: {u.username}')
#
# for u in Chats.objects.all():
#     print(f'ID: {u.id} \ttitle: {u.title}')

