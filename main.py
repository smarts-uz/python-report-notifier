import sys
import os

from Parsing.getdialogs import collect_dialogs
from Parsing.userDialogs import save_dialogs_to_db

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
import django
django.setup()

from dotenv import load_dotenv
chat_id = os.getenv("CHAT_ID")
chat_id_2 = os.getenv("CHAT_ID_2")

load_dotenv()
from TGBOT.tgbot import creatTopic
sys.dont_write_bytecode = True
import click

from db.save_to_db import *
from datetime import datetime


from logx import Logger
add_keyword_log = Logger('add_keyword',"a")
add_report_log = Logger('add_report',"a")
command_line_log = Logger('command_line',"a")




#Click command start
@click.command()
@click.argument('new_keyword', type=str)
def add_keyword(new_keyword):
    create_topic = creatTopic(new_keyword,chat_id)
    topic_id = create_topic
    click.echo(f'Topic "{new_keyword}" has created successfully!')
    try:
        from db.models import Keyword
        Keyword.objects.get_or_create(name=new_keyword,
                           topic_id=topic_id,
                            last_checked=datetime(2015,1,1))
        add_keyword_log.log(f'[DB]{new_keyword} created successfully ')
        print(f'[DB]{new_keyword} created successfully ')
    except Exception as e:
        add_keyword_log.err(e)
    click.echo(f'Keyword "{new_keyword}" added successfully!')

@click.command()
@click.argument('new_report',type=str)
def add_report(new_report):
    try:
        create_topic = creatTopic(new_report, chat_id_2)
        report = save_to_report(new_report,create_topic)
        click.echo(f'[report][added]: {new_report}')
        add_report_log.log(f'[report][added]: {new_report}')
    except Exception as e:
        click.echo(f'[Some kind of error] check the log file!!!')
        add_report_log.err(f'[Some kind of error]: {e}')



@click.command()
def show_keywords():
    data = Keyword.objects.values('name',)
    click.echo(list(data))



@click.command()
def run_searching():
    save_to_db()
    click.echo('*----searching successfully finished----*')

@click.command()
def collect_msg_group():
    save_db_rss_group()
    click.echo('*-------------end-----------*')


@click.command()
def collect_msg_channel():
    save_db_rss_channel()
    click.echo('*-------------end-----------*')


@click.command()
def get_rating():
    save_to_rating()
    click.echo('[Reply Messages process successfully ended!!]')


@click.command()
def get_dialogs():
    save_dialogs_to_db()
    collect_dialogs()
    click.echo("[Process: Collect Dialog ended!]")


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

try:
    if __name__ == '__main__':
        cli()
        msg = "Searching successfully ended!"
        command_line_log.log(msg)
except Exception as e:
    msg = "Some kind of error, check log file"
    print(msg)
    command_line_log.log(msg)
    command_line_log.err(e)


#Click command end!






