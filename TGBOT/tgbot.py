import os

from telebot import TeleBot

from dotenv import load_dotenv
from logx import Logger
sendM = Logger('sendMessage', 'a')
forwM = Logger('forwardMessage', 'a')
creatT = Logger('creatTopic', 'a')
from regexF.regexFunction import retry_after

load_dotenv()
token = os.getenv("TOKEN")


bot = TeleBot(token, parse_mode="HTML")


def sendMsg(content,date,message_link,topic_id,chat_id,user_id,user_fullname,tg_id,chat_title,username=None):
    if username == None:
        text = f"""📝  {content}

👉  <a href="{message_link}">Message</a>
👥  <a href="t.me/c/{tg_id}">{chat_title}</a>
👤  <a href="t.me/@id{user_id}">{user_fullname}</a>
📅  {date}"""
    else:
        text = f"""📝  {content}
        
👉  <a href="{message_link}">Message</a>
👥  <a href="t.me/c/{tg_id}">{chat_title}</a>
👤  <a href="t.me/@{username}">{user_fullname}</a>
📅  {date}"""
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



def fwr_msg(user_id, user_fullname, chat_title, date, message_link, msg_id, peer_id,topic_id,chat_id,username=None):
    if  username ==None:
        text = f"""👉  <a href="{message_link}">Message</a>
👥  <a href="t.me/c/{peer_id}">{chat_title}</a>
👤  <a href="t.me/@id{user_id}">{user_fullname}</a>
📅  {date}"""
    else:
        text = f"""👉  <a href="{message_link}">Message</a>
👥  <a href="t.me/c/{peer_id}">{chat_title}</a>
👤  <a href="t.me/@{username}">{user_fullname}</a>
📅  {date}"""


   
    try:

        a = bot.forward_message(chat_id=chat_id, from_chat_id=peer_id, message_id=msg_id, timeout=10,message_thread_id=topic_id)

        fwr_id = a.json['message_id']
        print(f'[Message forward]  id {fwr_id}')
        forwM.log(f'[Forward Message]{a}')
    except Exception as e:
        if 'telebot.apihelper.ApiTelegramException: A request to the Telegram API was unsuccessful. Error code: 400. Description: Bad Request: chat not found' == e:
            print(f'Please add bot to this group: {peer_id}')
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
        a = bot.create_forum_topic(chat_id=chat_id,name=name,)
        topic_id = a.message_thread_id
        topic_title = a.name
        creatT.log(f'[Create Topic] : {topic_title}')
    except Exception as e:
        print(f'[Creat Topic Error]')
        creatT.err(f'[Error] : {e}')
        topic_id = None

    return topic_id





