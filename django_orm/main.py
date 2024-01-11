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

def db_check():
    response = ""
    query = input("Enter query: ")
    response = Keyword.objects.filter(name__icontains=query)
    first_row = response.first()
    if response.exists():
        # print(first_row.last_checked, query)
        return first_row.last_checked, query
    else:
        new = Keyword.objects.create(
            name = query,
            last_checked = datetime.min
        )
        new.save()
        new_row = response.first()
        # print(new_row.last_checked, query)
        return  new_row.last_checked, query

a = db_check()
print("Time:", a[0],"\nQ:", a[1])


# query = input("Enter query: ")
# response = Keyword.objects.filter(name__icontains=query)
# fm = response.first()
# print(response, fm)