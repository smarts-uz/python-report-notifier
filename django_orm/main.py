import sys
import time
from Parsing.forward_msg import ForwardMsg

from Parsing.craeteTopic import CreateTopic
from Parsing.send_msg import sendMessage
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

from logx import Logger
save_to_db = Logger('save_to_db', 'w')
add_keyword_log = Logger('add_keyword',"a")
save_to_db_chat = Logger('save_to_db_chat', 'w')
save_to_db_user = Logger('save_to_db_user', 'w')
save_to_db_message = Logger('save_to_db_message', 'w')

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


def all_keywords():
    data = Keyword.objects.values('pk', 'name', 'last_checked', "topic_id")
    return list(data)


def forward_message_boolen(peer_id):
    chat = Chat.objects.get(peer_id=peer_id)
    return chat.forward_message


def get_title_chat(peer_id):
    chat = Chat.objects.get(peer_id=peer_id)
    return chat.title


def get_user_fullname(user_id):
    user = User.objects.get(user_id=user_id)
    return user.fullname, user.username


def get_msg_id(msg_full_link):
    message = Message.objects.get(message_full_link=msg_full_link)
    return message.first.pk


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
                save_to_db_chat.log(chat)
            except Exception as e:
                save_to_db_chat.err(e)


        # Saving users data to db
        users = parser.users()
        for user in users:
            try:
                User.objects.get_or_create(**user)
                print(
                f'[Keyword: {item["name"]}][User has been saved]: user_id: {user["user_id"]}  fullname : {user["fullname"]} username: {user["username"]}')
                save_to_db_user.log(user)
            except Exception as e:
                save_to_db_user.err(e)

        # Saving messages data to db
        messages = parser.messages()
        for message in messages:
            message['keyword_id'] = item['pk']
            msg_id = message['msg_id_field']
            try:
                Message.objects.get_or_create(**message)
                save_to_db_message.log(message)
            except Exception as e:
                save_to_db_message.err(e)
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
                # sendMessage(str(content), user_link, str(private_chat_link), str(date), str(message_full_link),
                #             user_fullname, chat_title, username, topic_id, pk)  #python requests

            else:
                fwr_msg(user_link, user_fullname, chat_title, private_chat_link, date, message_full_link, msg_id, peer_id,
                        pk, username, topic_id)
                # forward_message = ForwardMsg(peer_id, msg_id, topic_id, user_link, date, user_fullname,
                #                              private_chat_link, chat_title,
                #                              message_full_link)
                #
                # rpl_msg = forward_message.replyMessage()   #python requests

            print(
                f'[Keyword: {item["name"]}][Message has been saved]: content: {message["content"]} ,chat_id:  {message["peer_id"]}, user_id: {message["user_id"]}, time: {message["datetime"]} private_chat_link: {message["private_chat_link"]}')

        time.sleep(1)

        update_time = parser.update_date()
        print("last checked time", update_time)

        key = Keyword.objects.get(name=item["name"])
        # Do something with the 'key' object


        key.last_checked = update_time
        key.save()
        print(f'update time is {update_time}')
        print(f"f[*---------{item['name']}-------------- search successfully ended!! *]")

    for i in range(5):
        print(i + 1)
        time.sleep(1)


    print("Successfully end!!!!")





@click.command()
def run_searching():
    save_to_db()
    click.echo('*----searching successfully finished----*')


@click.group()
def cli():
    pass


cli.add_command(add_keyword)
cli.add_command(show_keywords)
cli.add_command(run_searching)

if __name__ == '__main__':
    cli()

