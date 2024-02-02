# ORM functionality
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
import django
django.setup()

# .env
from dotenv import load_dotenv
load_dotenv()
chat_id = os.getenv("CHAT_ID")
chat_id_2 = os.getenv("CHAT_ID_2")

# Other packages
import time
from Parsing.parser import Parser
from Parsing.Telegram_RSS import rss_group ,rss_channel
from db.db_functions import *
from TGBOT.tgbot import sendMsg, fwr_msg, creatTopic
from datetime import datetime

now =datetime.now()

# Logger
from logx import Logger
log_names = ['save_to_db', 'save_to_report', 'rss_parsing_save_to_db', 'save_to_rating']
save_to_db_log = Logger(log_names[0], 'a')
save_to_report_log = Logger(log_names[1], 'a')
rss_parsing_save_to_db = Logger(log_names[2],"a")
save_to_rating_log = Logger(log_names[3], 'a')

def save_to_db():
    print("Parsing in progress...")
    for item in all_keywords():
        parser = Parser(item['last_checked'], item['name'])
        # Saving chats data to db
        chats = parser.chats()
        for chat in chats:
            print(
                f"""✅ Chat has been saved!
Keyword: {item["name"]}
Chat ID: {chat["chat_id"]}
Chat Title: {chat["title"]}
Public Chat Link: {chat["public_chat_link"]}""")
            try:
                Chat.objects.get_or_create(**chat)
                print("Chat has been created!")
                save_to_db_log.log(chat)
            except Exception as e:
                print(f"<!> Oops! Something went wrong, check the log file: {save_to_db_log}.log!")
                save_to_db_log.err(e)

        # Saving users data to db
        users = parser.users()
        for user in users:
            try:
                User.objects.get_or_create(**user)
                print(
                f"""✅ User has been saved!
Keyword: {item["name"]}
User ID: {user["user_id"]}
Fullname : {user["fullname"]}
Username: {user["username"]}""")
                save_to_db_log.log(user)
            except Exception as e:
                print(f"<!> Oops! Something went wrong, check the log file: {save_to_db_log}.log")
                save_to_db_log.err(e)

        # Saving messages data to db
        messages = parser.messages()
        for message in messages:

            message['keyword_id'] = item['pk']
            msg_id = message['msg_id']
            try:
                Message.objects.get_or_create(**message)
                print("Message has been created!")
                save_to_db_log.log(message)
            except Exception as e:
                print(f"<!> Oops! Something went wrong, check the log file: {save_to_db_log}.log")
                save_to_db_log.err(e)
            user_link = message['user_link']
            content = message['content']
            date = message['datetime']
            peer_id = message['peer_id']
            private_chat_link = message['private_chat_link']
            message_full_link = message['message_full_link']
            user_id = message['user_id']
            topic_id = item['topic_id']
            tg_id = int(str(peer_id)[4:])
            forward_bool = forward_message_boolean(peer_id)
            chat_title = get_title_chat(peer_id)
            user_fullname = get_user_fullname(user_id)[0]
            username = get_user_fullname(user_id)[1]
            pk = item['pk']

            print(f"Forwarded: {forward_bool}")
            if forward_bool == True:
                sendMsg(content=content, user_id=user_id, tg_id=tg_id,date=date,message_link=message_full_link,user_fullname=user_fullname, chat_title=chat_title, username=username,
                        topic_id=topic_id,chat_id=chat_id)
            else:
                fwr_msg(user_id, user_fullname, chat_title, private_chat_link, date, message_full_link, msg_id, peer_id,
                        username, topic_id,chat_id)

            print(
                f"""✅ Message has been saved!
Keyword: {item["name"]}
Content: {message["content"]}
Chat ID:  {message["peer_id"]}
User ID: {message["user_id"]}
Time: {message["datetime"]}
Private Chat Link: {message["private_chat_link"]}""")

            time.sleep(1)

        update_time = parser.update_date()
        print("last checked time", update_time)

        key = Keyword.objects.get(name=item["name"])

        key.last_checked = update_time
        key.save()
        print(f'Update Time: {update_time}')
        print(f"*--- Searching for <{item['name']}> successfully ended! ---*")
        print('wait 5 sec to next keyword...')
        for i in range(5):
            print(i + 1)
            time.sleep(1)

    print("*--- Process has been successfully finished! ---*")



def save_db_rss_group():
    all_group = get_all_group()

    for group in all_group:
        if group['is_active']:
            print(group)
            peer_id = int(str(f'-100{group["tg_id"]}'))
            data = rss_group(peer_id, group['days_count'],group['forum'])
            messages = data[0]
            users = data[1]
            print(peer_id)

            for user in users:
                try:
                    try:
                        usr = TgGroupUser.objects.get(tg_group_user_id=user['tg_group_user_id'])
                        if user['full_name'] != usr.full_name:
                            
                            old_name = {f"{now}:full_name": usr.full_name}
                            ext_name = usr.old_full_name
                            ext_name.update(old_name)
                            usr.full_name = user['full_name']
                            
                            usr.save()
                            print(f'Group User Fullname with ID {user["tg_group_user_id"]} has been updated!')
                            rss_parsing_save_to_db.log(f"Group User Fullname updated: {user}")

                        if user['username'] != usr.username:
                            
                            old_user = {f"{now}:username": usr.username}
                            ext_username = usr.old_username
                            ext_username.update(old_user)
                            usr.username = user['username']
                            
                            usr.save()
                            print(f'Group User Username with ID {user["tg_group_user_id"]} has been updated!')
                            rss_parsing_save_to_db.log(f"Group User Username updated: {user}")
                        if user['phone'] != usr.phone:
                            
                            old_phones = {f"{now}:phone": usr.phone}
                            ext_phone = usr.old_phone
                            ext_phone.update(old_phones)
                            usr.phone = user['phone']
                            
                            usr.save()
                            print(f'Group User Phone with ID {user["tg_group_user_id"]} has been updated!')
                            rss_parsing_save_to_db.log(f"Group User Phone updated: {user}")
                        else:
                            print('Group User already exists!')
                            rss_parsing_save_to_db.log(f"Group User - nothing updated: {user}!")


                    except TgGroupUser.DoesNotExist:
                        TgGroupUser.objects.create(**user)
                        print(f'User with ID {user["tg_group_user_id"]} has been saved to db!')
                        rss_parsing_save_to_db.log(f"User has been saved to db: {user}!")
                except Exception as e:
                    print("<!> Oops! Something went wrong, check the log file: {log_names[2]}.log")
                    rss_parsing_save_to_db.err(e)



            try:
                for message in messages:
                    if message['from_id'] != None:

                        message['tg_group_user_id'] = get_user_id_form_tg_group_user(message['from_id'])[0]
                        message['from_channel'] = get_user_id_form_tg_group_user(message['from_id'])[1]
                    message['tg_group_id'] = group['pk']
                    try:
                        msg = TgGroupMessage.objects.get(message_private_link=message['message_private_link'])
                        msg.tg_group_user_id = message['tg_group_user_id']

                        if message["content"] != msg.content:
                            if msg.content_history == None:
                                msg.content_history = {}

                            # ext_data.update(old)
                            msg.content_history.update({f"{message['edit_date']}" : msg.content})
                            msg.edit_date = message['edit_date']
                            msg.content = message["content"]
                            msg.replies_count = message['replies_count']
                            msg.save()

                            print(f'Message content with Link {message["message_private_link"]} has been updated!')
                            rss_parsing_save_to_db.log(f"Message has been updated: s{message}")
                        else:
                            msg.replies_count = message['replies_count']
                            msg.save()
                            print(f'Message with link  already exists {message["message_private_link"]}')
                            rss_parsing_save_to_db.log(f"Group already exists: {message}")
                        msg.save()

                    except TgGroupMessage.DoesNotExist:
                        TgGroupMessage.objects.create(**message)

                        print('Created a new Message')
                        print(f'Message with Link {message["message_private_link"]} has been saved to db!')
                        rss_parsing_save_to_db.log(f'Created a new message: {message}')
            # --------------

            except Exception as e:
                print('<!> Oops! Something went wrong, check the log file: {log_names[2]}.log')
                rss_parsing_save_to_db.err(e)
            print(f'Group with ID {peer_id} has been saved to DB!')
            rss_parsing_save_to_db.log(f'Group with ID {peer_id} has been saved to DB!')



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

                            old = {f"{message['edit_date']}:content": msg.content}

                            if msg.content_history == None:
                                msg.content_history = {}

                            msg.content_history.update(old)


                            msg.content = message["content"]
                            msg.save()

                            print(f'Channel message content with ID {message["message_private_link"]} has been updated!')
                            rss_parsing_save_to_db.log(f"Channel Message content updated: {message}")
                        else:
                            print(f'Channel message already exists: {message["message_private_link"]}')
                            rss_parsing_save_to_db.log(f"Channel Message already exists: {message}")


                    except TgChannelMessage.DoesNotExist:
                        TgChannelMessage.objects.create(**message)

                        print('Created a new message!')
                        print(f'Channel Message with link {message["message_private_link"]} has been saved to DB')
                        rss_parsing_save_to_db.log(f'New channel message created: {message}')

            # --------------

            except Exception as e:
                print('<!> Oops! Something went wrong, check the log file: {rss_parsing_save_to_db}.log')
                rss_parsing_save_to_db.err(e)

            print(f'Channel with peerID {peer_id} has been saved to DB!')
            rss_parsing_save_to_db.log(f'Channel with peerID {peer_id} has been saved to DB!')


def save_to_report(msg_private_link):
    try:
        title = get_title_from_user_and_message(msg_private_link)
        print(title)
        try:
            report = Report.objects.get(message_link=msg_private_link)
            if report.thread_id == None:
                thread_id = creatTopic(title, chat_id_2)
                report.thread_id = thread_id
                report.thread_title = title
                report.save()
                print(f'Report has been updated to {title}!')

            print('Report already exists!')
            save_to_report_log.log('Report already exists!')

        except Report.DoesNotExist:
            thread_id = creatTopic(title, chat_id_2)
            report = get_message_from_group(msg_private_link)
            peer_id = str(report[2])
            chats_id = int(str(peer_id)[4:])
            Report.objects.create(
                message_link=msg_private_link,
                topic_id=report[3],
                message_id=report[1],
                chat_id=chats_id,
                tg_group_message_id=report[0],
                replies_count=report[4],
                thread_id=thread_id,
                thread_title=title

            )
            print(f'{title} has been saved to DB!')
            save_to_report_log.log(f'{title} has been saved to DB!')
    except Exception as e:
            print(e)
            save_to_report_log.err(e)
            title = None


    return title

def save_to_rating():
    try:
        for report in get_all_reports():
            print(f'Report: {report}')
            reply_messages = get_reply_messages(report['message_id'])
            for rpl_msg in reply_messages:
                # print(f'[Reply Message] : {rpl_msg.pk}:{rpl_msg.message_private_link}')
                try:
                    rate = Rating.objects.get(message_private_link=rpl_msg.message_private_link)
                    print(f'Reply Message with ID {rpl_msg.message_private_link} already exists!')
                    if rate.content != rpl_msg.content:
                        rate.content = rpl_msg.content
                        rate.content_history = rpl_msg.content_history
                        rate.replies_count = rpl_msg.replies_count
                        rate.save()


                        print(f'Reply Message Content has been updated to {rpl_msg.content}!')
                        save_to_rating_log.log(f'Reply Message Content has been updated to {rpl_msg.content}!')

                    else:
                        rate.replies_count = rpl_msg.replies_count
                        rate.save()
                        save_to_rating_log.log(f'Reply Message with Link {rpl_msg.message_private_link} already exists!')
                except Rating.DoesNotExist:
                    Rating.objects.create(
                        content=rpl_msg.content,
                        msg_id=rpl_msg.msg_id,
                        from_id=rpl_msg.from_id,
                        peer_id=rpl_msg.peer_id,
                        date=rpl_msg.date,
                        reply_to_msg_id=rpl_msg.reply_to_msg_id,
                        topic_id=rpl_msg.topic_id,
                        tg_group_message_id=rpl_msg.pk,
                        message_private_link=rpl_msg.message_private_link,
                        message_public_link=rpl_msg.message_public_link,
                        content_history=rpl_msg.content_history,
                        report_id=report['pk']

                    )
                    forward_bool = get_forward(rpl_msg.peer_id)
                    full_name = get_fullname_from_rating(rpl_msg.from_id)

                    tg_id = int(str(rpl_msg.peer_id)[4:])

                    chat_title =get_title_from_collect_group(tg_id)
                    if forward_bool != False:
                        sendMsg(content=rpl_msg.content, date=rpl_msg.date,
                                        message_link=rpl_msg.message_private_link,  topic_id=report['thread_id'],
                                        chat_id=chat_id_2,user_id=rpl_msg.from_id,user_fullname=full_name,tg_id=tg_id,chat_title=chat_title)
                    else:
                        fwr_msg(user_id=rpl_msg.from_id,user_fullname=full_name, chat_title=chat_title,peer_id=rpl_msg.peer_id, date=rpl_msg.date, message_link=rpl_msg.message_private_link, msg_id=rpl_msg.msg_id,
                                topic_id=report['thread_id'], chat_id=chat_id_2)


                    print(f'{rpl_msg.message_private_link} added to rating table!')
                    print(f'Saving Reply Message process with link {report["message_link"]} succesfully ended!')
            save_to_rating_log.log(f'Saving Reply Message process with link {report["message_link"]} succesfully ended!')
    except Exception as e:
        print(f'<!> Oops! Something went wrong, check the log file: {log_names[3]}.log')
        save_to_rating_log.err(e)


def foreach_report():
    reports = get_thread_id_and_title_from_report()
    for report in reports:

        msg_link = report.message_link
        title = get_title_from_user_and_message(msg_link)
        thread_id = creatTopic(title, chat_id_2)
        report = get_message_from_group(msg_link)
        peer_id = str(report[2])
        chats_id = int(str(peer_id)[4:])
        print(f'****[ {title} ] topic created in group!!****')
        update_report = Report.objects.get(message_link=msg_link)
        update_report.topic_id = report[3]
        update_report.message_id = report[1]
        update_report.chat_id = chats_id
        update_report.tg_group_message_id = report[0]
        update_report.replies_count = report[4]
        update_report.thread_id=thread_id
        update_report.thread_title=title
        update_report.save()


def save_to_keyword(keyword):
    try:
        key = Keyword.objects.get(name=keyword)
        if key.topic_id == None:
            topic_id = creatTopic(keyword,chat_id)
            key.topic_id = topic_id
            if key.last_checked == None:
                key.last_checked = datetime(2015,1,1)
                print(f'last checked time set to default {key.last_checked}')
            key.save()
            print(f'********** {keyword}\'s topic_id updated to {topic_id} **********')
        else:
            print(f'******* {keyword} is already exist *******')
    except Keyword.DoesNotExist:
        topic_id = creatTopic(keyword, chat_id)
        Keyword.objects.create(
            name = keyword,
            last_checked = datetime(2015,1,1),
            topic_id = topic_id
        )
        print(f'********** {keyword} created successfully! **********')


def foreach_keyword():
    try:
        keywords = get_name_from_keyword()
        for keyword in keywords:
            name = keyword.name
            topic_id = creatTopic(name, chat_id_2)
            key = Keyword.objects.get(name=name)
            key.topic_id = topic_id
            if key.last_checked == None:
                key.last_checked = datetime(2015, 1, 1)
                print(f'last checked time set to default {key.last_checked}')
            key.save()
            print(f'****[ {name} ] topic created in group!!****')
    except Exception as e:
        #loggin
        print('<!> Oops! Something went wrong, check the log file: {save_to_rating_log}.log')
        save_to_rating_log.err(e)



