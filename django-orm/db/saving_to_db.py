from models import *
import sys

sys.dont_write_bytecode = True

# Django specific settings
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
import django

django.setup()


def get_data(name):
    keyword = Keyword.objects.get(name=name)

    return keyword.last_checked


print(get_data("#report"))


def update_data(pk, updated_date):
    keyword = Keyword.objects.get(pk=pk)
    keyword.last_checked = updated_date
    keyword.save()
    return updated_date
