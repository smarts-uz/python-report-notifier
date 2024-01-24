from  datetime import datetime,timedelta
import  requests
from pprint import pprint
def rss(peer_id,days):
    messages = []
    users = []
    topics = []
    pag = 0
    while True:
        pag +=1
        tdz = 0
        today = datetime.now()
        d = today - timedelta(days=days)
        timestamp = datetime.timestamp(d)

        url = f"http://192.168.0.111:9504/json/{peer_id}/{pag}"
        response = requests.post(url).json()




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
            new_data = {
                    "contact" : contact,
                    "bot" : bot,
                    "tg_group_user_id" :tg_group_user_id,
                    "full_name" :fullname,
                    "username" : username,
                    "phone" : phone,
                    "photo_field" : photo,
                    "status" : status,
                    "tg_group_id" : tg_group_id,
                    "mtproto" : mtproto
                }


            if not any(item["tg_group_user_id"] == new_data["tg_group_user_id"] for item in users):
                users.append(
                new_data
                )
            else:

                continue




 #-------messages ----
        for message in response['messages']:

            tdz = message['date']
            if message['_'] == 'messageService':
                continue
            type = message['_']
            noforwards = message.get('noforwards',' ')
            id = message['id']
            from_id = message.get('from_id',' ')
            peer_id = message['peer_id']
            date_timestamp = message['date']
            date = datetime.fromtimestamp(date_timestamp)
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
                edit_date_timestamp = message['edit_date']
                edit_date = datetime.fromtimestamp(edit_date_timestamp)
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
            messages.append({
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


            if timestamp >= tdz:
                break
        print(f"Lenth User: {len(users)}")
        print(f"Lenth Messages: {len(messages)}")
        print(f'{timestamp} and {tdz}')

        if timestamp >= tdz:
            break
    return messages , users ,topics

#
# r = rss('-1002109564785',30)
# pprint(r[1])
# pprint(r[0])