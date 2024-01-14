from telegram import ParseMode
import telegram

import os
from dotenv import load_dotenv

load_dotenv()


def send_msg(content, user_link, private_chat_link, date, message_link):
    token = os.getenv("TOKEN")
    chat_id = os.getenv("CHAT_ID")

    text = f"""№ ---
    
📅<b>Date</b> : <u>{date}</u>
👤<b>User</b> : {user_link}
👥<b>Group/Channel</b> : <a href="{private_chat_link}">Chat Link</a>
🔗<b>Link</b>: <a href="{message_link}">Message Link</a>

📩<b>Text</b>: <i>{content}</i> """
    print(f"user_link  : {user_link}")

    bot = telegram.Bot(token=token)
    bot.sendMessage(chat_id=chat_id, text=text, parse_mode=ParseMode.HTML)
