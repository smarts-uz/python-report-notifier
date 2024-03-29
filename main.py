# ORM functionality
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
import django
django.setup()

# .env functionality
from dotenv import load_dotenv
load_dotenv()
chat_id = os.getenv("CHAT_ID")
chat_id_2 = os.getenv("CHAT_ID_2")

# Other packages
import sys

from TGBOT.tgbot import creatTopic
from datetime import datetime
sys.dont_write_bytecode = True
import click
from Parsing.getdialogs import collect_dialogs
from Parsing.userDialogs import save_dialogs_to_db
from Parsing.getForumTopic import check_topics

# ORM imports
from db.save_to_db import *
from db.models import Keyword

# Logger
from logx import Logger
add_keyword_n, add_report_n, command_line_n = 'add_keyword', 'add_report', 'command_line'
add_keyword_log = Logger(f'{add_keyword_n}', "a",subdirectory='command_line')
add_report_log = Logger(f'{add_report_n}', "a",subdirectory='command_line')
command_line_log = Logger(f'{command_line_n}', "a",subdirectory='command_line')


# Click - used to create CLI functionality
@click.command()
def add_keyword():
    new_keyword = input("Input your search keyword: ")
    try:
        save_to_keyword(new_keyword)
        print(f'*****Progress successfully ended!!!*****')
    except Exception as e:
        msg = f"<!> Oops! Something went wrong, check the log file: {command_line_n}.log"
        print(msg)
        command_line_log.err(e)


@click.command()
def add_report():
    new_report = input("Put message link: ")
    try:
        save_to_report(new_report)
        print(f'***** Progress successfully ended!!! ***** ')
    except Exception as e:
        msg = f"<!> Oops! Something went wrong, check the log file: {command_line_n}.log"
        print(msg)
        command_line_log.err(e)



@click.command()
def show_keywords():
    data = Keyword.objects.values('name',)
    click.echo(list(data))


@click.command()
def run_searching():
    save_to_db()
    click.echo('*---- Searching finished! ----*')


@click.command()
def collect_msg_group():
    save_db_rss_group()
    click.echo('*--- Group Message Collection Process Finished! ---*')


@click.command()
def collect_msg_channel():
    save_db_rss_channel()
    click.echo('*--- Channel Message Collection Process Finished! ---*')


@click.command()
def get_rating():
    save_to_rating()
    click.echo('*--- Reply Messages Process Finished! ---*')


@click.command()
def get_dialogs():
    save_dialogs_to_db()
    collect_dialogs()
    click.echo("*--- Collect Dialogs Process Finished! ---*")

@click.command()
def check_report():
    try:
        foreach_report()
        print('*****Progress successfully ended!!*****')
    except Exception as e:
        msg = f"<!> Oops! Something went wrong, check the log file: {command_line_n}.log"
        print(msg)
        command_line_log.err(e)

@click.command()
def check_keyword():
    try:
        foreach_keyword()
        print('*****Progress successfully ended!!*****')
    except Exception as e:
        msg = "<!> Oops! Something went wrong, check the log file: {command_line_n}.log"
        print(msg)
        command_line_log.err(e)



@click.group()
def cli():
    pass


cli.add_command(add_keyword)
cli.add_command(show_keywords)
cli.add_command(run_searching)
cli.add_command(collect_msg_group)
cli.add_command(collect_msg_channel)
cli.add_command(add_report)
cli.add_command(get_rating)
cli.add_command(get_dialogs)
cli.add_command(check_keyword)
cli.add_command(check_report)



try:
    if __name__ == '__main__':
        cli()
        msg = "*--- Searching successfully ended! ---*"
        command_line_log.log(msg)
except Exception as e:
    msg = f"<!> Oops! Something went wrong, check the log file: {command_line_n}.log"
    print(msg)
    command_line_log.err(e)
