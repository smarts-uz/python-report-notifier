import requests
from pprint import pprint
class Rss:

    def __init__(self,chat_id):
        self.chat_id = chat_id

    def parsing(self):
        url = f"http://192.168.3.54:9504/json/{self.chat_id}?limit=10"
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
        data = []
        response = self.parsing()
        for message in response['messages']:

            if message['_'] == 'messageService':
                continue
            type = message['_']
            noforwards = message.get('noforwards',' ')
            id = message['id']
            from_id = message['from_id']
            peer_id = message['peer_id']
            date = message['date']
            content = message['message']
            reply_to_top_id = None
            mtproto = message
            tg_group_id = None
            pinned = message['pinned']
            message_private_link = f"t.me/c/{int(str(peer_id)[4:])}/{id}"
            post = message['post']
            out = message['out']
            try :
                replies_count = message['replies']['replies']
                max_id = message['replies']['max_id']
                read_max_id = message['replies']['read_max_id']
                comments = message['replies']['comments']


            except Exception as e:
                replies_count = None
                max_id = None
                read_max_id = None
                comments = None
            try:
                media = message['media']
            except Exception as e:
                media = None

            try:
                edit_date = message['edit_date']
            except Exception as e:
                edit_date = None
            try:

                forum_topic = message['reply_to']['forum_topic']
                reply_to_msg_id  = message['reply_to']['reply_to_msg_id']
                try:
                    reply_to_top_id = message['reply_to']['reply_to_top_id']
                except Exception as e:
                    reply_to_top_id = None




            except Exception as e:
                forum_topic = None
                reply_to_msg_id = None
            data.append({
                "noforwards" : noforwards,
                "msg_id" : id,
                "from_id" : from_id,
                "peer_id" : peer_id,
                "date" : date,
                "content" : content,
                "forum_topic": forum_topic,
                "reply_to_msg_id": reply_to_msg_id,
                "topic_id" : reply_to_top_id,
                "mtproto" : mtproto,
                "tg_group_id" : tg_group_id,
                "edit_date" : edit_date,
                "message_private_link" : message_private_link,
                "type" : type,
                "pinned" : pinned,
                "media" : media,
                "post" : post,
                "out" : out,
                "replies_count" :replies_count,
                "max_id" :max_id,
                "read_max_id" : read_max_id,
                "comments" : comments







            })
        return data


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
            mtproto = user

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
                    "tg_group_id" : tg_group_id,
                    "mtproto" : mtproto
                }
            )
        return data


    def category(self):
        response = self.parsing()
        for i in response:
            print(i)









chat_id= -1002109564785
#
# rss = Rss(chat_id).messages()
# # rss = Rss(chat_id).category()
# pprint(rss)