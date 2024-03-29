# .env functionality
import os
from dotenv import load_dotenv
load_dotenv()
ip = os.getenv("IP")
port = os.getenv("PORT_RSS")

# Other packages
from datetime import datetime,timedelta
import requests



from logx import Logger
log_file_name = 'telegram_rss_parsing'
telegram_rss_parsing_log = Logger(log_file_name, 'a',subdirectory='parsing')


def rss_group(peer_id, days,forum):
    forum = forum
    messages, users, topics = [], [], []
    public_link = None
    pag = 0
    try:
        while True:
            pag += 1
            tdz = 0
            today = datetime.now()
            d = today - timedelta(days=days)
            timestamp = datetime.timestamp(d)

            url = f"http://{ip}:{port}/json/{peer_id}/{pag}"
            response = requests.post(url).json()

            for chat in response['chats']:
                try:
                    username = chat['username']
                except Exception:
                    username = None
                if username is not None:
                    public_link = f'https://t.me/{username}'
                else:
                    public_link = None

            try:
                for user in response['users']:
                    tg_group_id = None
                    contact = user['contact']
                    bot = user['bot']
                    tg_group_user_id = user['id']
                    fullname = f'{user.get("first_name", " ")} {user.get("last_name", " ")}'
                    username = user.get('username', None)
                    phone = user.get("phone", "hidden")
                    photo = user.get("photo", None)
                    status = user.get("status", None)
                    mtproto = user
                    new_data = {
                        "contact": contact,
                        "bot": bot,
                        "tg_group_user_id": tg_group_user_id,
                        "full_name": fullname,
                        "username": username,
                        "phone": phone,
                        "photo_field": photo,
                        "status": status,
                        "tg_group_id": tg_group_id,
                        "mtproto": mtproto
                    }
                    if not any(item["tg_group_user_id"] == new_data["tg_group_user_id"] for item in users):
                        telegram_rss_parsing_log.log(new_data)
                        users.append(
                            new_data
                        )
                    else:
                        continue
            except Exception as e:
                msg = f"<!> Oops! Something went wrong, check the log file: {log_file_name}.log"
                print(msg)
                telegram_rss_parsing_log.err(e)



            # ---- messages ----
            try:
                for message in response['messages']:
                    from_channel = None
                    tdz = message['date']
                    if message['_'] == 'messageService':
                        continue
                    type = message['_']
                    noforwards = message.get('noforwards', None)
                    id = message['id']
                    from_id = message.get('from_id', None)
                    peer_id = message['peer_id']
                    date_timestamp = message['date']
                    date = datetime.fromtimestamp(date_timestamp)
                    content = message['message']
                    reply_to_msg_id = None
                    topic_id = None
                    mtproto = message
                    tg_group_id = None
                    reply_to = None
                    tg_group_user_id = None
                    pinned = message['pinned']
                    post = message['post']
                    out = message['out']
                    try:
                        replies_count = message['replies']['replies']
                        max_id = message['replies']['max_id']
                        read_max_id = message['replies']['read_max_id']
                        comments = message['replies']['comments']

                    except Exception:
                        replies_count = None
                        max_id = None
                        read_max_id = None
                        comments = None
                    try:
                        media = message['media']
                    except Exception:
                        media = None

                    try:
                        edit_date_timestamp = message['edit_date']
                        edit_date = datetime.fromtimestamp(edit_date_timestamp)
                    except Exception:
                        edit_date = None
                    try:
                        reply_to = message['reply_to']
                        forum_topic = reply_to['forum_topic']
                        if forum_topic == False:
                            topic_id = None
                            reply_to_msg_id = reply_to['reply_to_msg_id']
                        else:
                            topic_id = reply_to['reply_to_msg_id']
                            try:
                                topic_id = reply_to['reply_to_top_id']
                                reply_to_msg_id = reply_to['reply_to_msg_id']
                            except Exception:
                                topic_id = reply_to['reply_to_msg_id']

                    except Exception:
                        forum_topic = None
                        reply_to = None
                    if topic_id is not None:
                        message_private_link = f"https://t.me/c/{int(str(peer_id)[4:])}/{topic_id}/{id}"
                    else:
                        if forum == False:
                            message_private_link = f"https://t.me/c/{int(str(peer_id)[4:])}/{id}"
                        else:
                            message_private_link = f"https://t.me/c/{int(str(peer_id)[4:])}/1/{id}"
                    if public_link is not None:
                        if topic_id is not None:
                            message_public_link = f'{public_link}/{topic_id}/{id}'
                        else:

                            message_public_link = f'{public_link}/{id}'
                    else:
                        message_public_link = None

                    messages.append({
                        "noforwards": noforwards,
                        "msg_id": id,
                        "from_id": from_id,
                        "peer_id": peer_id,
                        "date": date,
                        "content": content,
                        "forum_topic": forum_topic,
                        "reply_to_msg_id": reply_to_msg_id,
                        "topic_id": topic_id,
                        "mtproto": mtproto,
                        "tg_group_id": tg_group_id,
                        "edit_date": edit_date,
                        "message_public_link": message_public_link,
                        "message_private_link": message_private_link,
                        "type": type,
                        "pinned": pinned,
                        "media": media,
                        "post": post,
                        "out": out,
                        "replies_count": replies_count,
                        "max_id": max_id,
                        "read_max_id": read_max_id,
                        "comments": comments,
                        "tg_group_user_id": tg_group_user_id,
                        "from_channel": from_channel
                    })
                    telegram_rss_parsing_log.log(message)

                    if timestamp >= tdz:
                        break
                print(f"Total users found: {len(users)}")
                print(f"Total messages found: {len(messages)}")
                print(f'{timestamp} and {tdz}')
                if timestamp >= tdz:
                    break

            except Exception as e:
                msg = f"<!> Oops! Something went wrong, check the log file: {log_file_name}.log"
                print(msg)
                telegram_rss_parsing_log.err(e)
    except Exception as e:
        msg = f"<!> Oops! Something went wrong, check the log file: {log_file_name}.log"
        print(msg)
        telegram_rss_parsing_log.err(e)
    return messages, users


def rss_channel(peer_id,days):
    messages = []
    public_link = None
    reply = None
    pag = 0
    while True:
        pag += 1
        tdz = 0
        today = datetime.now()
        d = today - timedelta(days=days)
        timestamp = datetime.timestamp(d)

        url = f"http://{ip}:{port}/json/{peer_id}/{pag}"
        response = requests.post(url).json()
        try:

            for chat in response['chats']:
                try:
                    username = chat['username']
                except Exception:
                    username = None
                if username is not None:
                    public_link = f'https://t.me/{username}'
                else:
                    public_link = None
                telegram_rss_parsing_log.log(chat)

        except Exception as e:
            msg = f"<!> Oops! Something went wrong, check the log file: {log_file_name}.log"
            print(msg)
            telegram_rss_parsing_log.err(e)
        try:
            for message in response['messages']:

                tdz = message['date']
                if message['_'] == 'messageService':
                    continue
                type = message['_']
                noforwards = message.get('noforwards', None)
                id = message['id']

                peer_id = message['peer_id']
                date_timestamp = message['date']
                date = datetime.fromtimestamp(date_timestamp)
                content = message['message']
                reply_to_top_id = None
                mtproto = message
                tg_channel_id = None
                pinned = message['pinned']
                message_private_link = f"https://t.me/c/{int(str(peer_id)[4:])}/{id}"
                if public_link is not None:
                    message_public_link = f'{public_link}/{id}'
                else:
                    message_public_link = None
                post = message['post']
                out = message['out']
                try:
                    replies_count = message['replies']['replies']
                    max_id = message['replies']['max_id']
                    read_max_id = message['replies']['read_max_id']
                    comments = message['replies']['comments']
                except Exception:
                    replies_count = None
                    max_id = None
                    read_max_id = None
                    comments = None

                try:
                    views = message['views']
                except Exception:
                    views = None
                try:
                    media = message['media']
                except Exception:
                    media = None

                try:
                    edit_date_timestamp = message['edit_date']
                    edit_date = datetime.fromtimestamp(edit_date_timestamp)
                except Exception:
                    edit_date = None
                try:
                    forum_topic = message['reply_to']['forum_topic']
                    reply_to_msg_id = message['reply_to']['reply_to_msg_id']
                    try:
                        reply_to_top_id = message['reply_to']['reply_to_top_id']
                    except Exception:
                        reply_to_top_id = None
                except Exception:
                    forum_topic = None
                    reply_to_msg_id = None
                    reply_to_top_id = None

                messages.append({
                    "noforwards": noforwards,
                    "msg_id": id,
                    "peer_id": peer_id,
                    "date": date,
                    "content": content,
                    "forum_topic": forum_topic,
                    "reply_to_message_id": reply_to_msg_id,
                    "topic_id": reply_to_top_id,
                    "mtproto": mtproto,
                    "tg_channel_id": tg_channel_id,
                    "edit_date": edit_date,
                    "message_public_link": message_public_link,
                    "message_private_link": message_private_link,
                    "type": type,
                    "pinned": pinned,
                    "media": media,
                    "post": post,
                    "out": out,
                    "replies_count": replies_count,
                    "max_id": max_id,
                    "read_max_id": read_max_id,
                    "comments": comments,
                    "views": views
                })

                if timestamp >= tdz:
                    break
            print(f"Total messages found: {len(messages)}")
            print(f'{timestamp} and {tdz}')
            if timestamp >= tdz:
                break
        except Exception as e:
            msg = f"<!> Oops! Something went wrong, check the log file: {log_file_name}.log"
            print(msg)
            telegram_rss_parsing_log.err(e)

    return messages


