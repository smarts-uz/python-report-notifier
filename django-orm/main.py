############################################################################
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

import datetime

now = datetime.datetime.now()

current_timestamp = datetime.datetime.now().astimezone().isoformat()


# Seed a few users in the database
# Keyword.objects.create(
#     name='#report',
#     last_checked = now
# )
# Keyword.objects.create(
#     name='#LeftTheOffice',
#     last_checked = now
# )

def get_data(name):
    keyword = Keyword.objects.get(name=name)

    return keyword.last_checked


print(get_data("#report"))


def update_data(pk, updated_date):
    keyword = Keyword.objects.get(pk=pk)
    keyword.last_checked = updated_date
    keyword.save()
    return updated_date

dd = update_data(6,now)
print(get_data('#report'))

#
# for u in Keyword.objects.all():
#     print(f'ID: {u.id} \tUsername: {u.name} \tlast_checked: {u.last_checked}')
