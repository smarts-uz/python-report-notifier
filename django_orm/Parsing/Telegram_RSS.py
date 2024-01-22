import requests
from pprint import pprint
class Rss:

    def __init__(self,chat_id):
        self.chat_id = chat_id

    def parsing(self):
        url = f"http://192.168.3.54:9504/json/{self.chat_id}?limit=100"
        response = requests.post(url).json()
        return response

    def topic(self):
        response = self.parsing()
        data = []
        for topic in response['topics']:
            topic_id = topic["id"]
            created_time = topic['date']
            title = topic['title']
            topic_creater_id = topic['from_id']
            closed = topic['closed']
            data.append({
                "tg_topic_id" : topic_id,
                "created_time" : created_time,
                "title" : title,
                "topic_creater_id" :topic_creater_id,
                "closed" : closed

            })
        return data






#
# chat_id= -1002109564785
#
# rss = Rss(chat_id).topic()
# pprint(rss)