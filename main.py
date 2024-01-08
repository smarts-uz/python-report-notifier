from pprint import pprint
from datetime import datetime

import requests

now = datetime.now()
current_timestamp = datetime.timestamp(now)

url = "http://192.168.3.54:9503/api/messages.searchGlobal"

payload = {"params": {
    "flags": 0,
    "filter": {"_": "inputMessagesFilterEmpty"},
    "folder_id": None,
    "q": "#report",
    "min_date": 1704450000,

    "max_date": f"{current_timestamp}",
    "offset_peer": {"_": "inputPeerEmpty"},
    "offset_id": 0,
    "limit": 100
}}
headers = {"content-type": "application/json"}

response = requests.get(url, json=payload, headers=headers).json()
# type = response['response']['chats'][0]["_"]
# url = response['response']['messages'][0]["entities"][3]["url"]
#
users = response['response']['users']
for user in users:

    lname = user.get("last_name",' ')

    name = f'{user["first_name"]} {lname}'
    username = user['username']
    print(name)
    print(username)
# --------------------------------------------------------------
"""extracting text from_id timestamp from response['messages']"""

# msgs = response['response']['messages']
# for msg in msgs:
#     text = msg['message']
#     from_id = msg['from_id']
#     timestamp = msg['date']
#     # print(msg)
# --------------------------------------------------------------

# --------------------------------------------------------------------------------------------------
# import requests
# import json
#
# url = "http://127.0.0.1:9503/api/messages.search"
#
# payload = json.dumps({
#     "params": {
#         "flags": 0,
#         "filter": {
#             "_": "inputMessagesFilterEmpty"
#         },
#         "folder_id": None,
#         "q": "#report",
#         "offset_date": 0,
#         "offset_peer": {
#             "_": "inputPeerChat",
#             "chat_id": -1002109564785
#         },
#         "offset_id": 0,
#         "limit": 10
#     }
# })
# headers = {
#     'Content-Type': 'application/json'
# }
#
# response = requests.request("GET", url, headers=headers, data=payload)
#
# print(response.text)
