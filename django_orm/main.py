import sys
import time
from Parsing.forward_msg import ForwardMsg

from Parsing.craeteTopic import CreateTopic
from Parsing.send_msg import sendMessage

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


@click.command()
@click.argument('new_keyword', type=str)
def add_keyword(new_keyword):
    cr_topic = CreateTopic(new_keyword)
    topic_id = cr_topic.craeteTopic()
    click.echo(f'Topic "{new_keyword}" has created successfully!')
    Keyword.objects.get_or_create(name=new_keyword,
                           topic_id=topic_id)
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
            Chat.objects.get_or_create(**chat)

        # Saving users data to db
        users = parser.users()
        for user in users:
            User.objects.get_or_create(**user)
            print(
                f'[Keyword: {item["name"]}][User has been saved]: user_id: {user["user_id"]}  fullname : {user["fullname"]} username: {user["username"]}')

        # Saving messages data to db
        messages = parser.messages()
        for message in messages:
            message['keyword_id'] = item['pk']
            msg_id = message['msg_id_field']
            Message.objects.get_or_create(**message)
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


                sendMessage(str(content), user_link, str(private_chat_link), str(date), str(message_full_link),
                            user_fullname, chat_title, username, topic_id, pk)

            else:

                forward_message = ForwardMsg(peer_id, msg_id, topic_id, user_link, date, user_fullname,
                                             private_chat_link, chat_title,
                                             message_full_link)

                rpl_msg = forward_message.replyMessage()

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
