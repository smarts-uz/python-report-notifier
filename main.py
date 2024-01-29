import sys
import time

from TGBOT.tgbot import sendMsg,fwr_msg,creatTopic
sys.dont_write_bytecode = True
import click
# Django specific settings
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
import django

django.setup()
from db.models import *
from datetime import datetime
from Parsing.parser import Parser
from Parsing.Telegram_RSS import Rss

from logx import Logger
save_to_db_log = Logger('save_to_db', 'a')
add_keyword_log = Logger('add_keyword',"a")


#------- django orm function start

from db.db_functions import *



#django orm function end


# ----------save to db start
def save_to_db():
    print("[Parsing in progress]")
    for item in all_keywords():
        parser = Parser(item['last_checked'], item['name'])
        # Saving chats data to db
        chats = parser.chats()
        for chat in chats:
            print(
                f'[Keyword: {item["name"]}][Chat has been saved]: chat_id:{chat["chat_id"]}  chat_title:{chat["title"]} public_chat_link: {chat["public_chat_link"]}')
            try:
                Chat.objects.get_or_create(**chat)
                save_to_db_log.log(chat)
            except Exception as e:
                save_to_db_log.err(e)

        # Saving users data to db
        users = parser.users()
        for user in users:
            try:
                User.objects.get_or_create(**user)
                print(
                f'[Keyword: {item["name"]}][User has been saved]: user_id: {user["user_id"]}  fullname : {user["fullname"]} username: {user["username"]}')
                save_to_db_log.log(user)
            except Exception as e:
                save_to_db_log.err(e)

        # Saving messages data to db
        messages = parser.messages()
        for message in messages:
            message['keyword_id'] = item['pk']
            msg_id = message['msg_id_field']
            try:
                Message.objects.get_or_create(**message)
                save_to_db_log.log(message)
            except Exception as e:
                save_to_db_log.err(e)
            user_link = message['user_link']
            content = message['content']
            date = message['datetime']
            peer_id = message['peer_id']
            private_chat_link = message['private_chat_link']
            message_full_link = message['message_full_link']
            user_id = message['user_id']
            topic_id = item['topic_id']

            forward_bool = forward_message_boolen(peer_id)
            chat_title = get_title_chat(peer_id)
            user_fullname = get_user_fullname(user_id)[0]
            username = get_user_fullname(user_id)[1]
            pk = item['pk']

            print(f"[Forward]:{forward_bool}")
            if forward_bool == True:
                sendMsg(content, user_link, private_chat_link, date, message_full_link, user_fullname, chat_title, username,
                        topic_id, pk)
            else:
                fwr_msg(user_link, user_fullname, chat_title, private_chat_link, date, message_full_link, msg_id, peer_id,
                        pk, username, topic_id)

            print(
                f'[Keyword: {item["name"]}][Message has been saved]: content: {message["content"]} ,chat_id:  {message["peer_id"]}, user_id: {message["user_id"]}, time: {message["datetime"]} private_chat_link: {message["private_chat_link"]}')

        time.sleep(1)

        update_time = parser.update_date()
        print("last checked time", update_time)

        key = Keyword.objects.get(name=item["name"])

        key.last_checked = update_time
        key.save()
        print(f'update time is {update_time}')
        print(f"f[*---------{item['name']}-------------- search successfully ended!! *]")

        for i in range(5):
            print(i + 1)
            time.sleep(1)

    print("Successfully end!!!!")



def save_db_rss():
    messages =Rss(-1002109564785).messages()
    for message in messages:
        try:
         TgGroupMessage.objects.get_or_create(**message)
        except Exception as e:
            print(e)




#save to db end



#Click command start
@click.command()
@click.argument('new_keyword', type=str)
def add_keyword(new_keyword):
    create_topic = creatTopic(new_keyword)
    topic_id = create_topic
    click.echo(f'Topic "{new_keyword}" has created successfully!')
    try:
        Keyword.objects.get_or_create(name=new_keyword,
                           topic_id=topic_id)
        add_keyword_log.log(f'{new_keyword} created successfully ')
    except Exception as e:
        add_keyword_log.err(e)
    click.echo(f'Keyword "{new_keyword}" added successfully!')


@click.command()
def show_keywords():
    data = Keyword.objects.values('name',)
    click.echo(list(data))



@click.command()
def run_searching():
    save_to_db()
    click.echo('*----searching successfully finished----*')

@click.command()
def run_rss():
    save_db_rss()
    click.echo('*-------------end-----------*')

from Parsing.userDialogs import save_dialogs_to_db
@click.command()
def collect_dialogs():
    save_dialogs_to_db()

    click.echo('*----collect ended!!!!---*')


@click.group()
def cli():
    pass



cli.add_command(add_keyword)
cli.add_command(show_keywords)
cli.add_command(run_searching)
cli.add_command(run_rss)
cli.add_command(collect_dialogs)


try:
    if __name__ == '__main__':
        cli()
        msg = "Searching successfully ended!"
        save_to_db_log.log(msg)
except Exception as e:
    msg = "Some kind of error, check log file"
    print(msg)
    save_to_db_log.log(msg)
    save_to_db_log.err(e)


#Click command end!







