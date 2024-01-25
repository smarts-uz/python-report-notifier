import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
import django
import time
django.setup()

from datetime import datetime
from Parsing.parser import Parser
from Parsing.Telegram_RSS import rss_group ,rss_channel
from db.db_functions import *
from TGBOT.tgbot import sendMsg,fwr_msg

from logx import Logger
save_to_db_log = Logger('save_to_db', 'a')

rss_parsing_save_to_db = Logger('rss_parsing_save_to_db',"a")

def save_to_db():
    print("[Parsing in progress]")
    for item in all_keywords():
        parser = Parser(item['last_checked'], item['name'])
        # Saving chats data to db
        chats = parser.chats()
        for chat in chats:
            print(
                f'[Keyword: {item["name"]}][Chat has been saved]: chat_id:{chat["chat_id"]}  chat_title:{chat["title"]} public_chat_link: {chat["public_chat_link"]}')
            try:

                Chat.objects.get_or_create(**chat)
                save_to_db_log.log(chat)
            except Exception as e:
                save_to_db_log.err(e)

        # Saving users data to db
        users = parser.users()
        for user in users:
            try:
                User.objects.get_or_create(**user)
                print(
                f'[Keyword: {item["name"]}][User has been saved]: user_id: {user["user_id"]}  fullname : {user["fullname"]} username: {user["username"]}')
                save_to_db_log.log(user)
            except Exception as e:
                save_to_db_log.err(e)

        # Saving messages data to db
        messages = parser.messages()
        for message in messages:
            message['keyword_id'] = item['pk']
            msg_id = message['msg_id_field']
            try:
                Message.objects.get_or_create(**message)
                save_to_db_log.log(message)
            except Exception as e:
                save_to_db_log.err(e)
            user_link = message['user_link']
            content = message['content']
            date = message['datetime']
            peer_id = message['peer_id']
            private_chat_link = message['private_chat_link']
            message_full_link = message['message_full_link']
            user_id = message['user_id']
            topic_id = item['topic_id']

            forward_bool = forward_message_boolen(peer_id)
            chat_title = get_title_chat(peer_id)
            user_fullname = get_user_fullname(user_id)[0]
            username = get_user_fullname(user_id)[1]
            pk = item['pk']

            print(f"[Forward]:{forward_bool}")
            if forward_bool == True:
                sendMsg(content, user_link, private_chat_link, date, message_full_link, user_fullname, chat_title, username,
                        topic_id, pk)
            else:
                fwr_msg(user_link, user_fullname, chat_title, private_chat_link, date, message_full_link, msg_id, peer_id,
                        pk, username, topic_id)

            print(
                f'[Keyword: {item["name"]}][Message has been saved]: content: {message["content"]} ,chat_id:  {message["peer_id"]}, user_id: {message["user_id"]}, time: {message["datetime"]} private_chat_link: {message["private_chat_link"]}')

        time.sleep(1)

        update_time = parser.update_date()
        print("last checked time", update_time)

        key = Keyword.objects.get(name=item["name"])

        key.last_checked = update_time
        key.save()
        print(f'update time is {update_time}')
        print(f"f[*---------{item['name']}-------------- search successfully ended!! *]")

        for i in range(5):
            print(i + 1)
            time.sleep(1)

    print("Successfully end!!!!")



def save_db_rss_group():
    all_group = get_all_group()

    for group in all_group:
        if group['is_active']:
            print(group)
            peer_id = int(str(f'-100{group["tg_id"]}'))

            data = rss_group(peer_id, group['days_count'])
            messages = data[0]
            users = data[1]
            print(peer_id)
            try:
                for message in messages:
                    message['tg_group_id'] = group['pk']
                    try:
                        msg = TgGroupMessage.objects.get(message_private_link=message['message_private_link'])
                        if message["content"] != msg.content:
                            count = msg.old_count + 1
                            old = {f"{count}:content": msg.content}
                            ext_data = msg.old_content

                            ext_data.update(old)
                            msg.old_count = count

                            msg.content = message["content"]
                            msg.save()

                            print(f'[Group]content update {message["message_private_link"]}')
                            rss_parsing_save_to_db.log(f"[UPDATED MESSAGE]{message}")
                        else:
                            print(f'[Group]already exists {message["message_private_link"]}')
                            rss_parsing_save_to_db.log(f"[Group][ALREADY EXISTS]{message}")


                    except TgGroupMessage.DoesNotExist:
                        TgGroupMessage.objects.create(**message)

                        print('[Group]Created new message')
                        print(f'[Group][Message has been saved to db] msg_id : {message["message_private_link"]}')
                        rss_parsing_save_to_db.log(f'[Group][CREATED NEW MESSAGE] {message}')
            # --------------

            except Exception as e:
                print('[Group][Message][Some Kind of error check the log file]')
                rss_parsing_save_to_db.err(f'[Group][Message Error]: {e}')
            for user in users:
                try:
                    try:
                        usr = TgGroupUser.objects.get(tg_group_user_id=user['tg_group_user_id'])
                        if user['full_name'] != usr.full_name:
                            count = usr.old_full_name_count + 1
                            old_name = {f"{count}:full_name": usr.full_name}
                            ext_name = usr.old_full_name
                            ext_name.update(old_name)
                            usr.full_name = user['full_name']
                            usr.old_full_name_count = count
                            usr.save()
                            print(f'[Group][user][full_name] updated {user["tg_group_user_id"]}')
                            rss_parsing_save_to_db.log(f"[Group][UPDATED FULLNAME]{user}")

                        if user['username'] != usr.username:
                            count = usr.old_username_count + 1
                            old_user = {f"{count}:username": usr.username}
                            ext_username = usr.old_username
                            ext_username.update(old_user)
                            usr.username = user['username']
                            usr.old_username_count = count
                            usr.save()
                            print(f'[Group][user][username] updated {user["tg_group_user_id"]}')
                            rss_parsing_save_to_db.log(f"[Group][UPDATED USERNAME]{user}")
                        if user['phone'] != usr.phone:
                            count = usr.old_phone_count + 1
                            old_phones = {f"{count}:phone": usr.phone}
                            ext_phone = usr.old_phone
                            ext_phone.update(old_phones)
                            usr.phone = user['phone']
                            usr.old_phone_count = count
                            usr.save()
                            print(f'[Group][user][phone] updated {user["tg_group_user_id"]}')
                            rss_parsing_save_to_db.log(f"[Group][UPDATED PHONE]{user}")
                        else:
                            print('[Group]user already exist')
                            rss_parsing_save_to_db.log(f"[Group][NOTHING UPDATE]: {user}")


                    except TgGroupUser.DoesNotExist:
                        TgGroupUser.objects.create(**user)
                        print(f'[Group][User has been saved to db] user_id :  {user["tg_group_user_id"]}')
                        rss_parsing_save_to_db.log(f"[Group][User has been saved to db] {user}")
                except Exception as e:
                    print('[Group][User][Some Kind of error check the log file]')
                    rss_parsing_save_to_db.err(f'[Group][User error]: {e}')
            print(f'[Group][{peer_id}] : saving to db successfully end!')
            rss_parsing_save_to_db.log(f'[Group][{peer_id}] : saving to db successfully end!')


def save_db_rss_channel():
    all_group = get_all_channel()

    for group in all_group:
        if group['is_active']:
            print(group)
            peer_id = int(str(f'-100{group["tg_id"]}'))

            data = rss_channel(peer_id, group['days_count'])
            messages = data

            print(peer_id)
            try:
                for message in messages:
                    message['tg_channel_id'] = group['pk']
                    try:
                        msg = TgChannelMessage.objects.get(message_private_link=message['message_private_link'])
                        if message["content"] != msg.content:
                            count = msg.old_count + 1
                            old = {f"{count}:content": msg.content}
                            ext_data = msg.old_content

                            ext_data.update(old)
                            msg.old_count = count

                            msg.content = message["content"]
                            msg.save()

                            print(f'[Channel][Message]content update {message["message_private_link"]}')
                            rss_parsing_save_to_db.log(f"[Channel][UPDATED MESSAGE]{message}")
                        else:
                            print(f'[Channel]already exists {message["message_private_link"]}')
                            rss_parsing_save_to_db.log(f"[Channel][ALREADY EXISTS]{message}")


                    except TgChannelMessage.DoesNotExist:
                        TgChannelMessage.objects.create(**message)

                        print('[Channel]Created new message')
                        print(f'[Channel][Message has been saved to db] msg_id : {message["message_private_link"]}')
                        rss_parsing_save_to_db.log(f'[Channel][CREATED NEW MESSAGE] {message}')

            # --------------

            except Exception as e:
                print('[Channel][Message][Some Kind of error check the log file]')
                rss_parsing_save_to_db.err(f'[Message Error]: {e}')

            print(f'[Channel][{peer_id}] : saving to db successfully end!')
            rss_parsing_save_to_db.log(f'[Channel][{peer_id}] : saving to db successfully end!')


Keyword.objects.create(name=777)