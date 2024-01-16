import requests



def craeteTopic(name):
    url = "https://api.telegram.org/bot6454237457:AAHcoiiJ4gw-Zb9HCbJtHN8HiLkwHlsG474/createForumTopic"

    payload = {
        "chat_id": "-1002059626462",
        "name": f"{name}",
        "icon_color": "16766590 "
    }
    headers = {"content-type": "application/json"}

    response = requests.post(url, json=payload, headers=headers)

    print(response.json())

