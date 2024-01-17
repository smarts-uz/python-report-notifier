from telebot import TeleBot

import os
from dotenv import load_dotenv

from regexF.regexFunction import retry_after

load_dotenv()
token = os.getenv("TOKEN")
chat_id = os.getenv("CHAT_ID")

bot = TeleBot(token, parse_mode="HTML")


def sendMsg(content, user_link, private_chat_link, date, message_link, user_fullname, chat_title, username, topic_id,pk):
    text = f"""<b>🔢:{pk}</b>

    📅<b>Date</b> : <u>{date}</u>
    👤<b>User</b> :  <a href="t.me/{username}">{user_fullname}</a>
    🔗<b>User Link</b> : <tg-spoiler>{user_link}</tg-spoiler>
    👥<b>Group/Channel</b> : <a href="{private_chat_link}">{chat_title}</a>
    🔗<b>Link</b>: <a href="{message_link}">Message Link</a>

    📩<b>Text</b>: <i>{content}</i> """
    try:
        a = bot.send_message(chat_id=chat_id,message_thread_id=topic_id,text=text,timeout=10)
        print(a)
    except Exception as e:
        print((f'[Error] {e}'))
        retry_after(str(e))
        a = bot.send_message(chat_id=chat_id, message_thread_id=topic_id, text=text, timeout=10)
        print(a)



def fvr_msg(user_link, user_fullname, chat_title, private_chat_link, date, message_link, msg_id, peer_id, pk,username, topic_id):
    text = f"""(PY)<b>№:</b>

    📅<b>Date</b> : <u>{date}</u>
    👤<b>User</b> :  <a href="t.me/{username}">{user_fullname}</a>
    🔗<b>User Link</b> : <tg-spoiler>{user_link}</tg-spoiler>
    👥<b>Group/Channel</b> : <a href="{private_chat_link}">{chat_title}</a>
    🔗<b>Link</b>: <a href="{message_link}">Message Link</a>


    """
    # print(f"user_link  : {user_link}")

    a = bot.forward_message(chat_id=chat_id, from_chat_id=-1002098866683, message_id=63, timeout=10)

    fvr_id = a.json['message_id']


    bot.send_message(chat_id=chat_id,text=text, reply_to_message_id=fvr_id, timeout=10)








