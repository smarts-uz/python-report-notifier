from datetime import datetime
from .TOKEN import *
from telegram import ParseMode
from Parsing.parser import Parser
import telegram

char = list("_*[]()~`>#+-=|{}.")


def send_msg(content, user_link, private_chat_link, date, message_link):
    token = TOKEN
    chat_id = CHAT_ID

    text = f"""№ ---
    
📅<b>Date</b> : <u>{date}</u>
👤<b>User</b> : {user_link}
👥<b>Group/Channel</b> : <a href="{private_chat_link}">Chat Link</a>
🔗<b>Link</b>: <a href="{message_link}">Message Link</a>

📩<b>Text</b>: <i>{content}</i> """
    print(f"user_link  : {user_link}")

    bot = telegram.Bot(token=token)
    bot.sendMessage(chat_id=chat_id, text=text, parse_mode=ParseMode.HTML)
