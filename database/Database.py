from .models import *

def get_last_timestamp(pk):
    keyword = Keyword.objects.get(pk=pk)
    last_timestamp = keyword.last_checked
    return last_timestamp

def update_timestamp(pk,current_timestamp):
    keyword = Keyword.objects.get(pk=pk)
    keyword.last_checked(current_timestamp)
    keyword.save()
    print('timestamp has been changed!!!!')

