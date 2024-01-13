from datetime import datetime



from Parsing.parser import Parser
import telegram



def send_msg(text):
    token = '6454237457:AAHcoiiJ4gw-Zb9HCbJtHN8HiLkwHlsG474'
    chat_id = "-1001949412980"
    bot = telegram.Bot(token=token)
    bot.sendMessage(chat_id=chat_id, text=text)


p = Parser(datetime(2010, 1, 1), "#reopen")
#
for i in p.messages():
    user_id = i['user_id']
    content = i['content']
    date = i['datetime']

    
    send_msg(str(i))