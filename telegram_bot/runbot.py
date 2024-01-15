from telegram import ParseMode
import telegram

import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("TOKEN")
chat_id = os.getenv("CHAT_ID")


def send_msg(content, user_link, private_chat_link, date, message_link,user_fullname,chat_title,pk):
    text = f"""<b>№:{pk}</b>
    
📅<b>Date</b> : <u>{date}</u>
👤<b>User</b> :  <a href="{user_link}">{user_fullname}</a>
🔗<b>User Link</b> : <tg-spoiler>{user_link}</tg-spoiler>
👥<b>Group/Channel</b> : <a href="{private_chat_link}">{chat_title}</a>
🔗<b>Link</b>: <a href="{message_link}">Message Link</a>

📩<b>Text</b>: <i>{content}</i> """
    print(f"user_link  : {user_link}")

    bot = telegram.Bot(token=token)

    bot.sendMessage(chat_id=chat_id, text=text, parse_mode=ParseMode.HTML)


# def forward_msg(user_link, private_chat_link, date, message_link, msg_id, peer_id):
#     text = f"""№ ---
#
# 📅<b>Date</b> : <u>{date}</u>
# 👤<b>User</b> : {user_link}
# 👥<b>Group/Channel</b> : <a href="{private_chat_link}">Chat Link</a>
# 🔗<b>Link</b>: <a href="{message_link}">Message Link</a>
#
# """
#     print(f"user_link  : {user_link}")
#
#     bot = telegram.Bot(token=token)
    bot.forward_message(chat_id=chat_id, from_chat_id=peer_id, message_id=msg_id)


