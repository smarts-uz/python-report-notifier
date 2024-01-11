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

# def db_check():
#     response = ""
#     now = datetime.now()
#     current_timestamp = datetime.timestamp(now)
#     result = False
#     query = input("Enter query: ")
#     try:
#             response = Keyword.objects.filter(name__icontains=query)
#             print(response)
#             if response is True:
#                 return natija.lastcked


#     except:
#             Keyword.objects.create(
#                 name = answer,
#                 last_checked = now
#             )
#             Keyword.save()
#             return "True"




#     # for i in natija:

query = input("Enter query: ")
response = Keyword.objects.filter(name__icontains=query)
print(response)