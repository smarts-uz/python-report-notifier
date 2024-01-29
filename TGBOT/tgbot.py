from telebot import TeleBot

import os
from dotenv import load_dotenv
from logx import Logger
sendM = Logger('sendMessage', 'a')
forwM = Logger('forwardMessage', 'a')
creatT = Logger('creatTopic', 'a')
from regexF.regexFunction import retry_after

load_dotenv()
token = os.getenv("TOKEN")


bot = TeleBot(token, parse_mode="HTML")


def sendMsg(content, user_link=None, private_chat_link=None, date=None, message_link=None, user_fullname=None, chat_title=None, username=None, topic_id=None,pk=None,chat_id=None):
    text = f"""<b>🔢:{pk}</b>

    📅<b>Date</b> : <u>{date}</u>
    👤<b>User</b> :  <a href="t.me/{username}">{user_fullname}</a>
    🔗<b>User Link</b> : <tg-spoiler>{user_link}</tg-spoiler>
    👥<b>Group/Channel</b> : <a href="{private_chat_link}">{chat_title}</a>
    🔗<b>Link</b>: <a href="{message_link}">Message Link</a>

    📩<b>Text</b>: <i>{content}</i> """
    try:
        a = bot.send_message(chat_id=chat_id,message_thread_id=topic_id,text=text,timeout=10)
        print('[Message sent]')
        sendM.log(f'[Send Message] : {a}')
    except Exception as e:
        print(f'[Send Error] {e}')
        sendM.err(f'[Send Error] {e}')
        retry_after(str(e))
        a = bot.send_message(chat_id=chat_id, message_thread_id=topic_id, text=text, timeout=10)
        sendM.log(f'[Send Message] : {a}')
        print('[Message sent]')



def fwr_msg(user_link, user_fullname, chat_title, private_chat_link, date, message_link, msg_id, peer_id, pk,username, topic_id,chat_id):
    text = f"""<b>🔢:{pk}</b>

    📅<b>Date</b> : <u>{date}</u>
    👤<b>User</b> :  <a href="t.me/{username}">{user_fullname}</a>
    🔗<b>User Link</b> : <tg-spoiler>{user_link}</tg-spoiler>
    👥<b>Group/Channel</b> : <a href="{private_chat_link}">{chat_title}</a>
    🔗<b>Link</b>: <a href="{message_link}">Message Link</a>


    """
    # print(f"user_link  : {user_link}")
    try:
        a = bot.forward_message(chat_id=chat_id, from_chat_id=peer_id, message_id=msg_id, timeout=10,message_thread_id=topic_id)

        fwr_id = a.json['message_id']
        print(f'[Message forward]  id {fwr_id}')
        forwM.log(f'[Forward Message]{a}')
    except Exception as e:
        forwM.err(f'[Forward Error] {e}')
        print(f'[Forward Error] {e}')
        retry_after(str(e))

        a = bot.forward_message(chat_id=chat_id, from_chat_id=peer_id, message_id=msg_id, timeout=10,
                                message_thread_id=topic_id)


        fwr_id = a.json['message_id']
        print(f'[Message forwarded]  id {fwr_id}')
        forwM.log(f'[Forward Message]{a}')
    try:
        a = bot.send_message(chat_id=chat_id,text=text, reply_to_message_id=fwr_id, timeout=10,message_thread_id=topic_id)
        print('[Message sent]')
        forwM.log(f'[Reply Message] : {a}')

    except Exception as e:
        forwM.err(f'[Reply Error] : {e}')
        print((f'[Error] {e}'))
        retry_after(str(e))

        bot.send_message(chat_id=chat_id,text=text, reply_to_message_id=fwr_id, timeout=10,message_thread_id=topic_id)
        print('[Message sent]')
        forwM.log(f'[Reply Message] : {a}')






def creatTopic(name,chat_id):
    try:
        a = bot.create_forum_topic(chat_id=chat_id,name=name)
        topic_id = a.message_thread_id
        creatT.log(f'[Create Topic] : {a}')
    except Exception as e:
        print(f'[Creat Topic Error]')
        creatT.err(f'[Error] : {e}')
        topic_id = None

    return topic_id



def send_msg_rating(content,date,message_link,topic_id,chat_id):
    text = f"{content}"

    try:
        a = bot.send_message(chat_id=chat_id,message_thread_id=topic_id,text=text,timeout=10)
        print('[Message sent]')
        sendM.log(f'[Send Message] : {a}')
    except Exception as e:
        print(f'[Send Error] {e}')
        sendM.err(f'[Send Error] {e}')
        retry_after(str(e))
        a = bot.send_message(chat_id=chat_id, message_thread_id=topic_id, text=text, timeout=10)
        sendM.log(f'[Send Message] : {a}')
        print('[Message sent]')

def fwr_msg_rating(chat_id,peer_id,msg_id,topic_id):
    try:
        a = bot.forward_message(chat_id=chat_id, from_chat_id=peer_id, message_id=msg_id, timeout=10,
                                    message_thread_id=topic_id)

        fwr_id = a.json['message_id']
        print(f'[Message forward]  id {fwr_id}')
        forwM.log(f'[Forward Message]{a}')
    except Exception as e:
        forwM.err(f'[Forward Error] {e}')
        print(f'[Forward Error] {e}')
        retry_after(str(e))

        a = bot.forward_message(chat_id=chat_id, from_chat_id=peer_id, message_id=msg_id, timeout=10,
                                    message_thread_id=topic_id)

        fwr_id = a.json['message_id']
        print(f'[Message forwarded]  id {fwr_id}')
        forwM.log(f'[Forward Message]{a}')




# fwr_msg_rating(chat_id=-1001965260006, peer_id=-1002098866683, msg_id=89, topic_id=7)