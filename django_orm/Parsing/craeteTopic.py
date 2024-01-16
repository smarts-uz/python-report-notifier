import requests


class CreateTopic:

    def __init__(self,name):
        self.name = name




    def craeteTopic(self):
        url = "https://api.telegram.org/bot6454237457:AAHcoiiJ4gw-Zb9HCbJtHN8HiLkwHlsG474/createForumTopic"

        payload = {
            "chat_id": "-1002059626462",
            "name": f"{self.name}",
            "icon_color": "16766590 "
        }

        headers = {"content-type": "application/json"}

        response = requests.post(url, json=payload, headers=headers).json()
        topic_id = response['result']['message_thread_id']

        print(response)
        return topic_id


    # def get_topic_id(self):
    #     response = self.craeteTopic()
    #
    #     return topic_id




