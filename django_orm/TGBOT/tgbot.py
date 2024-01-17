from telebot import TeleBot

import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("TOKEN")
chat_id = os.getenv("CHAT_ID")

bot = TeleBot(token, parse_mode="HTML")


def sendMsg():
    a = bot.send_message(chat_id=chat_id, text="Hello 123",message_thread_id=1134,reply_to_message_id=1156)
    print(a['id'])



sendMsg()
