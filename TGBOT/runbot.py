from telegram import ParseMode, TelegramError
import telegram

import os
from dotenv import load_dotenv

from TGBOT.regex.regex import retry_after

load_dotenv()
token = os.getenv("TOKEN")
chat_id = os.getenv("CHAT_ID")


def send_msg(content, user_link, private_chat_link, date, message_link, user_fullname, chat_title, pk,username):
    text = f"""(PY)<b>№:{pk}</b>
    
📅<b>Date</b> : <u>{date}</u>
👤<b>User</b> :  <a href="t.me/{username}">{user_fullname}</a>
🔗<b>User Link</b> : <tg-spoiler>{user_link}</tg-spoiler>
👥<b>Group/Channel</b> : <a href="{private_chat_link}">{chat_title}</a>
🔗<b>Link</b>: <a href="{message_link}">Message Link</a>

📩<b>Text</b>: <i>{content}</i> """
    print(f"user_link  : {user_link}")

    bot = telegram.Bot(token=token)

    try:

        msg = bot.sendMessage(chat_id=chat_id, text=text, parse_mode=ParseMode.HTML, timeout=10)
        print(msg)
    except TelegramError as e:
        print((f'[Error] {e}'))
        retry_after(str(e))
        msg = bot.sendMessage(chat_id=chat_id, text=text, parse_mode=ParseMode.HTML, timeout=10)
        print(msg)


def forward_msg(user_link, user_fullname, chat_title, private_chat_link, date, message_link, msg_id, peer_id,pk,username):
    text = f"""(PY)<b>№:{pk}</b>

📅<b>Date</b> : <u>{date}</u>
👤<b>User</b> :  <a href="t.me/{username}">{user_fullname}</a>
🔗<b>User Link</b> : <tg-spoiler>{user_link}</tg-spoiler>
👥<b>Group/Channel</b> : <a href="{private_chat_link}">{chat_title}</a>
🔗<b>Link</b>: <a href="{message_link}">Message Link</a>


"""
    # print(f"user_link  : {user_link}")

    bot = telegram.Bot(token=token)
    try:

        fwr = forward = bot.forward_message(chat_id=chat_id,
                                            from_chat_id=peer_id,
                                            message_id=msg_id)
        print(fwr)
    except TelegramError as e:
        print((f'[Error] {e}'))
        retry_after(str(e))
        fwr = forward = bot.forward_message(chat_id=chat_id,
                                            from_chat_id=peer_id,
                                            message_id=msg_id)
        print(fwr)

    fw_msg_id = forward['message_id']
    try:
        msg = bot.sendMessage(chat_id=chat_id, text=text, parse_mode=ParseMode.HTML, reply_to_message_id=fw_msg_id, timeout=10)
        print(msg)
    except TelegramError as e:
        print((f'[Error] {e}'))
        retry_after(str(e))
        msg = bot.sendMessage(chat_id=chat_id, text=text, parse_mode=ParseMode.HTML, reply_to_message_id=fw_msg_id,
                              timeout=10)
        print(msg)

