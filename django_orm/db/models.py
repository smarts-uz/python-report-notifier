# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from datetime import datetime

from django.db import models


class Chat(models.Model):
    peer_id = models.BigIntegerField()
    type = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    chat_id = models.BigIntegerField(blank=True, null=True)
    public_chat_link = models.CharField(max_length=255, blank=True, null=True)
    forward_message = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'chat'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class Keyword(models.Model):
    name = models.CharField(max_length=255)
    last_checked = models.DateTimeField(blank=True, null=True, default=datetime(2015, 1, 1, 0, 0, 0))
    topic_link = models.CharField(max_length=255, blank=True, null=True)
    topic_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'keyword'


class Message(models.Model):
    datetime = models.DateTimeField(blank=True, null=True)
    keyword_id = models.IntegerField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    files = models.CharField(max_length=255, blank=True, null=True)
    user_id = models.BigIntegerField(blank=True, null=True)
    peer_id = models.BigIntegerField(blank=True, null=True)
    message_full_link = models.CharField(max_length=255, blank=True, null=True)
    public_chat_link = models.CharField(max_length=255, blank=True, null=True)
    private_chat_link = models.CharField(max_length=255, blank=True, null=True)
    user_link = models.CharField(max_length=255, blank=True, null=True)
    msg_id_field = models.IntegerField(db_column='msg_id ', blank=True,
                                       null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'message'


class TgGroupTexts(models.Model):
    type = models.CharField(max_length=255, blank=True, null=True)
    full_url = models.CharField(max_length=255, blank=True, null=True)
    tg_channel_text_id = models.IntegerField(blank=True, null=True)
    out = models.SmallIntegerField(blank=True, null=True)
    mentioned = models.SmallIntegerField(blank=True, null=True)
    media_unread = models.SmallIntegerField(blank=True, null=True)
    silent = models.SmallIntegerField(blank=True, null=True)
    post = models.SmallIntegerField(blank=True, null=True)
    from_scheduled = models.SmallIntegerField(blank=True, null=True)
    legacy = models.SmallIntegerField(blank=True, null=True)
    edit_hide = models.SmallIntegerField(blank=True, null=True)
    pinned = models.SmallIntegerField(blank=True, null=True)
    noforwards = models.SmallIntegerField(blank=True, null=True)
    tg_group_id = models.IntegerField(blank=True, null=True)
    tg_id = models.IntegerField(blank=True, null=True)
    from_id_field = models.CharField(db_column='from_id__', max_length=255, blank=True,
                                     null=True)  # Field renamed because it contained more than one '_' in a row. Field renamed because it ended with '_'.
    from_id_user_id = models.BinaryField(blank=True, null=True)
    peer_id_field = models.CharField(db_column='peer_id__', max_length=255, blank=True,
                                     null=True)  # Field renamed because it contained more than one '_' in a row. Field renamed because it ended with '_'.
    peer_id_channel_id = models.IntegerField(blank=True, null=True)
    fwd_from_field = models.CharField(db_column='fwd_from__', max_length=255, blank=True,
                                      null=True)  # Field renamed because it contained more than one '_' in a row. Field renamed because it ended with '_'.
    fwd_from_imported = models.SmallIntegerField(blank=True, null=True)
    fwd_from_from_id = models.TextField(blank=True, null=True)
    fwd_from_date = models.DateTimeField(blank=True, null=True)
    fwd_from_channel_post = models.IntegerField(blank=True, null=True)
    fwd_from_saved_from_peer = models.TextField(blank=True, null=True)
    fwd_from_saved_from_msg_id = models.IntegerField(blank=True, null=True)
    entities = models.TextField(blank=True, null=True)
    views = models.IntegerField(blank=True, null=True)
    reply_to_field = models.CharField(db_column='reply_to__', max_length=255, blank=True,
                                      null=True)  # Field renamed because it contained more than one '_' in a row. Field renamed because it ended with '_'.
    reply_to_reply_to_scheduled = models.SmallIntegerField(blank=True, null=True)
    reply_to_reply_to_msg_id = models.CharField(max_length=11, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    replies_field = models.CharField(db_column='replies__', max_length=255, blank=True,
                                     null=True)  # Field renamed because it contained more than one '_' in a row. Field renamed because it ended with '_'.
    replies_replies = models.IntegerField(blank=True, null=True)
    replies_comments = models.SmallIntegerField(blank=True, null=True)
    replies_replies_pts = models.IntegerField(blank=True, null=True)
    replies_max_id = models.IntegerField(blank=True, null=True)
    replies_read_max_id = models.IntegerField(blank=True, null=True)
    to_id_field = models.CharField(db_column='to_id__', max_length=255, blank=True,
                                   null=True)  # Field renamed because it contained more than one '_' in a row. Field renamed because it ended with '_'.
    to_id_channel_id = models.IntegerField(blank=True, null=True)
    media_field = models.CharField(db_column='media__', max_length=255, blank=True,
                                   null=True)  # Field renamed because it contained more than one '_' in a row. Field renamed because it ended with '_'.
    media = models.TextField(blank=True, null=True)
    action_field = models.CharField(db_column='action__', max_length=255, blank=True,
                                    null=True)  # Field renamed because it contained more than one '_' in a row. Field renamed because it ended with '_'.
    action = models.TextField(blank=True, null=True)
    dl_file_path = models.CharField(max_length=255, blank=True, null=True)
    dl_file_size = models.FloatField(blank=True, null=True)
    dl_status = models.SmallIntegerField(blank=True, null=True)
    replies_channel_id = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    mtproto = models.TextField(blank=True, null=True)
    keyword_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tg_group_texts'


class User(models.Model):
    user_id = models.BigIntegerField()
    username = models.CharField(max_length=255, blank=True, null=True)
    fullname = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'
