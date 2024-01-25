import sys
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
import django
django.setup()


from TGBOT.tgbot import sendMsg,fwr_msg,creatTopic
sys.dont_write_bytecode = True
import click
from db.models import *
from db.save_to_db import *



from logx import Logger
add_keyword_log = Logger('add_keyword',"a")




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
def collect_messages_g():
    save_db_rss_group()
    click.echo('*-------------end-----------*')


@click.command()
def collect_messages_c():
    save_db_rss_channel()
    click.echo('*-------------end-----------*')



@click.group()
def cli():
    pass



cli.add_command(add_keyword)
cli.add_command(show_keywords)
cli.add_command(run_searching)
cli.add_command(collect_messages_g)
cli.add_command(collect_messages_c)


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







