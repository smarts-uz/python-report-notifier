from datetime import datetime

from Parsing.parser import Parser
import telegram
from telegram import ParseMode


def send_msg(content, user_link, private_chat_link, date, message_link):
    token = '6454237457:AAHcoiiJ4gw-Zb9HCbJtHN8HiLkwHlsG474'
    chat_id = "-1001949412980"
    text = f"""
📅*Date* : {date},
👤*User* : [user link]({user_link}),
👥*Group/Channel* : [chat link]({private_chat_link}),
🔗*Link*: [message link]({message_link}),
📩*Text*: {content}

    
    
    """
    bot = telegram.Bot(token=token)
    bot.sendMessage(chat_id=chat_id, text=text, parse_mode=ParseMode.MARKDOWN_V2)

#
# p = Parser(datetime(2010, 1, 1), "#office")
# #
# for i in p.messages():
#     user_id = i['user_link']
#     content = i['content']
#     date = i['datetime']
#     private_chat_link = i['private_chat_link'],
#     message_full_link = i['message_full_link']
#     print(f"""{user_id},
#     {content},
#     {date},
#     {private_chat_link}
#     """)

    # send_msg(str(content), user_id, str(private_chat_link), str(date),str(message_full_link))
# send_msg("123","username","1238321d","2dasd","djsakn")

# push