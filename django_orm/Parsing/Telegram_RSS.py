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

    def messages(self):
        response = self.parsing()
        for message in response['messages']:
            pprint(message)


    def users(self):
        response = self.parsing()
        data = []
        for user in response['users']:
            tg_group_id = None
            contact = user['contact']
            bot = user['bot']
            tg_group_user_id = user['id']
            fullname = f'{user.get("first_name"," ")} {user.get("last_name"," ")}'
            username = user.get('username'," ")
            phone = user.get("phone","hidden")
            photo = user.get("photo"," ")
            status = user.get("status"," ")
            data.append(
                {
                    "contact" : contact,
                    "bot" : bot,
                    "tg_group_user_id" :tg_group_user_id,
                    "fullname" :fullname,
                    "username" : username,
                    "phone" : phone,
                    "photo" : photo,
                    "status" : status,
                    "tg_group_id" : tg_group_id
                }
            )
        return data


    def category(self):
        response = self.parsing()
        for i in response:
            print(i)










chat_id= -1002109564785

rss = Rss(chat_id).users()
# rss = Rss(chat_id).category()
pprint(rss)