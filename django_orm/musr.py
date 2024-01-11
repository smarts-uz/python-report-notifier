
from datetime import datetime

now = datetime.now()
#
# # Seed a few users in the database
# Keyword.objects.create(
#     name='#report1',
#     last_checked = now
# )
# Keyword.objects.create(
#     name='#LeftTheOffice2',
#     last_checked = now
# )
# #
# for u in Keyword.objects.all():
#     print(f'ID: {u.id} \tUsername: {u.name}')
#
# Users.objects.create(
#     user_id = 32153213,
#     username = 'supreme',
#     fullname = 'huiaskjn',
# )
#

# Message.objects.create(
#
#     name = 'rfiskwo',
#     datetime ='2023-12-16',
#     keyword_id = 1,
#     content = 'text',
#     from_id = 1235857,
#     peer_id = 4324234
# )


#
# for u in Message.objects.all():
#     print(f'ID: {u.id} \tpeer_id: {u.peer_id}')
#
for u in Chats.objects.all():
    print(f'ID: {u.id} \ttitle: {u.title}')

    #
    #
    # from Parsing.parser import Parser
    # p = Parser()
    # users = p.users()
    # for user in users:
    #     user_id = user['user_id']
    #     fullname = user['fullname']
    #     username = user['username']
    #     Users.objects.create(
    #         user_id = user_id,
    #         fullname = fullname,
    #         username = username
    #     )
    #     print('success')

    #
    # Users.objects.create(
    #         user_id = 764782,
    #         fullname = 'thdj',
    #         username = 'hurihq'
    #     )

from django_orm.Parsing.parser import Parser
p = Parser()
chats = p.chats()
for chat in chats:
    chat_id = chat['chat_id']
    type = chat['type']
    title = chat['title']
    Chats.objects.create(

        chat_id=chat_id,
        type=type,
        title=title

    )
    print(f'success id:{chat_id}')

from django_orm.db.models import *

#
# Users.objects.get_or_create(
#     user_id=764782,
#     fullname = 'thdj',
#     username = 'hurihq'
#
# )