

import requests
from pprint import pprint

url = "http://192.168.3.54:9503/api/messages.getDialogs"

response = requests.post(url).json()

for i in response['response']['chats']:
    print(i)