# from pprint import pprint
#
# import requests
# import datetime
# url = "http://127.0.0.1:9503/api/messages.searchGlobal"
#
# payload = { "params": {
#     "flags": 0,
#     "filter": { "_": "inputMessagesFilterEmpty" },
#     "folder_id": None,
#     "q": "smarts software",
#     "offset_date": 1703877600,
#     "offset_peer": { "_": "inputPeerEmpty" },
#     "offset_id": 0,
#     "limit": 1
#   } }
# headers = {"content-type": "application/json"}
#
# response = requests.get(url, json=payload, headers=headers).json()
# type = response['response']['chats'][0]["_"]
# url = response['response']['messages'][0]["entities"][3]["url"]
# #
# pprint(response['response']['messages'][0]["message"])
# #
# # for i in :
# #     pprint(i)


# --------------------------------------------------------------------------------------------------
import requests
import json

url = "http://127.0.0.1:9503/api/messages.search"

payload = json.dumps({
    "params": {
        "flags": 0,
        "filter": {
            "_": "inputMessagesFilterEmpty"
        },
        "folder_id": None,
        "q": "smarts software",
        "offset_date": 0,
        "offset_peer": {
            "_": "inputPeerChannel",
            "channel_id": -1001896684971
        },
        "offset_id": 0,
        "limit": 10
    }
})
headers = {
    'Content-Type': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
