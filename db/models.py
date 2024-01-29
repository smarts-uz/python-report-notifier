# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
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


class Keyword(models.Model):
    name = models.CharField(max_length=255)
    last_checked = models.DateTimeField(blank=True, null=True)
    topic_link = models.CharField(max_length=255, blank=True, null=True)
    topic_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'keyword'


class Message(models.Model):
    datetime = models.DateTimeField(blank=True, null=True)
    keyword = models.ForeignKey(Keyword, models.DO_NOTHING, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    files = models.CharField(max_length=255, blank=True, null=True)
    user_id = models.BigIntegerField(blank=True, null=True)
    peer_id = models.BigIntegerField(blank=True, null=True)
    message_full_link = models.CharField(max_length=255, blank=True, null=True)
    public_chat_link = models.CharField(max_length=255, blank=True, null=True)
    private_chat_link = models.CharField(max_length=255, blank=True, null=True)
    user_link = models.CharField(max_length=255, blank=True, null=True)
    msg_id = models.IntegerField(blank=True, null=True)
    message_public_link = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'message'


class Rating(models.Model):
    content = models.TextField(blank=True, null=True)
    msg_id = models.IntegerField(blank=True, null=True)
    from_id = models.BigIntegerField(blank=True, null=True)
    peer_id = models.BigIntegerField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    reply_to_msg_id = models.IntegerField(blank=True, null=True)
    topic_id = models.IntegerField(blank=True, null=True)
    tg_group_message = models.ForeignKey('TgGroupMessage', models.DO_NOTHING, blank=True, null=True)
    message_private_link = models.CharField(max_length=255, blank=True, null=True)
    message_public_link = models.CharField(max_length=255, blank=True, null=True)
    content_history = models.JSONField(blank=True, null=True)
    report = models.ForeignKey('Report', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rating'


class Report(models.Model):
    link = models.CharField(max_length=255, blank=True, null=True)
    topic_id = models.IntegerField(blank=True, null=True)
    message_id = models.IntegerField(blank=True, null=True)
    chat_id = models.IntegerField(blank=True, null=True)
    tg_group_message_id = models.IntegerField(blank=True, null=True)
    replies_count = models.BigIntegerField(blank=True, null=True)
    thread_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'report'


class TgChannel(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    tg_id = models.BigIntegerField()
    type = models.CharField(max_length=255, blank=True, null=True)
    invite_link = models.CharField(max_length=255, blank=True, null=True)
    bot_smarts_kick = models.SmallIntegerField(blank=True, null=True)
    bot_join_remove = models.SmallIntegerField(blank=True, null=True)
    restricted = models.CharField(max_length=255, blank=True, null=True)
    access_hash = models.CharField(max_length=255, blank=True, null=True)
    signatures = models.CharField(max_length=255, blank=True, null=True)
    read_inbox_max_id = models.IntegerField(blank=True, null=True)
    read_outbox_max_id = models.IntegerField(blank=True, null=True)
    hidden_prehistory = models.CharField(max_length=255, blank=True, null=True)
    bot_info = models.TextField(blank=True, null=True)
    notify_settings = models.TextField(blank=True, null=True)
    can_set_stickers = models.CharField(max_length=255, blank=True, null=True)
    can_view_participants = models.CharField(max_length=255, blank=True, null=True)
    can_set_username = models.CharField(max_length=255, blank=True, null=True)
    participants_count = models.CharField(max_length=255, blank=True, null=True)
    admins_count = models.IntegerField(blank=True, null=True)
    kicked_count = models.IntegerField(blank=True, null=True)
    banned_count = models.IntegerField(blank=True, null=True)
    migrated_from_chat_id = models.CharField(max_length=255, blank=True, null=True)
    migrated_from_max_id = models.CharField(max_length=255, blank=True, null=True)
    pinned_msg_id = models.CharField(max_length=255, blank=True, null=True)
    about = models.CharField(max_length=255, blank=True, null=True)
    can_view_stats = models.CharField(max_length=255, blank=True, null=True)
    online_count = models.CharField(max_length=255, blank=True, null=True)
    invite = models.CharField(max_length=255, blank=True, null=True)
    participants = models.TextField(blank=True, null=True)
    mtproto = models.JSONField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    hrm_project_id = models.IntegerField(blank=True, null=True)
    is_active = models.BooleanField(blank=True, null=True)
    days_count = models.IntegerField(blank=True, null=True)
    megagroup = models.BooleanField(blank=True, null=True)
    name_history = models.JSONField(blank=True, null=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    username_history = models.JSONField(blank=True, null=True)
    noforwards = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tg_channel'


class TgChannelMessage(models.Model):
    content = models.TextField(blank=True, null=True)
    noforwards = models.BooleanField(blank=True, null=True)
    msg_id = models.IntegerField(blank=True, null=True)
    peer_id = models.BigIntegerField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    forum_topic = models.BooleanField(blank=True, null=True)
    reply_to_message_id = models.IntegerField(blank=True, null=True)
    topic_id = models.IntegerField(blank=True, null=True)
    mtproto = models.JSONField(blank=True, null=True)
    tg_channel = models.ForeignKey(TgChannel, models.DO_NOTHING, blank=True, null=True)
    edit_date = models.DateTimeField(blank=True, null=True)
    message_private_link = models.CharField(max_length=255)
    type = models.CharField(max_length=255, blank=True, null=True)
    pinned = models.BooleanField(blank=True, null=True)
    media = models.JSONField(blank=True, null=True)
    post = models.BooleanField(blank=True, null=True)
    out = models.BooleanField(blank=True, null=True)
    replies_count = models.IntegerField(blank=True, null=True)
    max_id = models.IntegerField(blank=True, null=True)
    read_max_id = models.IntegerField(blank=True, null=True)
    comments = models.BooleanField(blank=True, null=True)
    content_history = models.JSONField(blank=True, null=True)
    message_public_link = models.CharField(max_length=255, blank=True, null=True)
    views = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tg_channel_message'


class TgGroup(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    linked_channel_id = models.IntegerField(blank=True, null=True)
    tg_id = models.BigIntegerField()
    type = models.CharField(max_length=255, blank=True, null=True)
    invite_link = models.CharField(max_length=255, blank=True, null=True)
    bot_smarts_kick = models.SmallIntegerField(blank=True, null=True)
    bot_join_remove = models.SmallIntegerField(blank=True, null=True)
    restricted = models.CharField(max_length=255, blank=True, null=True)
    access_hash = models.CharField(max_length=255, blank=True, null=True)
    signatures = models.CharField(max_length=255, blank=True, null=True)
    read_inbox_max_id = models.IntegerField(blank=True, null=True)
    read_outbox_max_id = models.IntegerField(blank=True, null=True)
    hidden_prehistory = models.CharField(max_length=255, blank=True, null=True)
    bot_info = models.TextField(blank=True, null=True)
    notify_settings = models.JSONField(blank=True, null=True)
    can_set_stickers = models.BooleanField(blank=True, null=True)
    can_view_participants = models.BooleanField(blank=True, null=True)
    can_set_username = models.BooleanField(blank=True, null=True)
    participants_count = models.IntegerField(blank=True, null=True)
    admins_count = models.IntegerField(blank=True, null=True)
    kicked_count = models.IntegerField(blank=True, null=True)
    banned_count = models.IntegerField(blank=True, null=True)
    migrated_from_chat_id = models.IntegerField(blank=True, null=True)
    migrated_from_max_id = models.IntegerField(blank=True, null=True)
    pinned_msg_id = models.IntegerField(blank=True, null=True)
    about = models.CharField(max_length=255, blank=True, null=True)
    can_view_stats = models.CharField(max_length=255, blank=True, null=True)
    online_count = models.CharField(max_length=255, blank=True, null=True)
    invite = models.CharField(max_length=255, blank=True, null=True)
    participants = models.CharField(max_length=255, blank=True, null=True)
    mtproto = models.JSONField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    hrm_project_id = models.IntegerField(blank=True, null=True)
    is_active = models.BooleanField(blank=True, null=True)
    name_history = models.JSONField(blank=True, null=True)
    last_message_id = models.BigIntegerField(blank=True, null=True)
    days_count = models.SmallIntegerField(blank=True, null=True)
    megagroup = models.BooleanField(blank=True, null=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    username_history = models.JSONField(blank=True, null=True)
    noforwards = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tg_group'


class TgGroupMessage(models.Model):
    content = models.TextField(blank=True, null=True)
    noforwards = models.BooleanField(blank=True, null=True)
    msg_id = models.IntegerField(blank=True, null=True)
    from_id = models.BigIntegerField(blank=True, null=True)
    peer_id = models.BigIntegerField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    forum_topic = models.BooleanField(blank=True, null=True)
    reply_to_msg_id = models.IntegerField(blank=True, null=True)
    topic_id = models.IntegerField(blank=True, null=True)
    mtproto = models.JSONField(blank=True, null=True)
    tg_group = models.ForeignKey(TgGroup, models.DO_NOTHING, blank=True, null=True)
    edit_date = models.DateTimeField(blank=True, null=True)
    message_private_link = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    pinned = models.BooleanField(blank=True, null=True)
    media = models.JSONField(blank=True, null=True)
    post = models.BooleanField(blank=True, null=True)
    out = models.BooleanField(blank=True, null=True)
    replies_count = models.CharField(max_length=255, blank=True, null=True)
    max_id = models.IntegerField(blank=True, null=True)
    read_max_id = models.IntegerField(blank=True, null=True)
    comments = models.BooleanField(blank=True, null=True)
    content_history = models.JSONField(blank=True, null=True)
    message_public_link = models.CharField(max_length=255, blank=True, null=True)
    tg_group_user_id = models.IntegerField(blank=True, null=True)
    tg_topic_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tg_group_message'


class TgGroupUser(models.Model):
    contact = models.BooleanField(blank=True, null=True)
    bot = models.BooleanField(blank=True, null=True)
    tg_group_user_id = models.BigIntegerField(blank=True, null=True)
    tg_group = models.ForeignKey(TgGroup, models.DO_NOTHING, blank=True, null=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    photo_field = models.JSONField(blank=True, null=True)
    status = models.JSONField(blank=True, null=True)
    mtproto = models.JSONField(blank=True, null=True)
    old_full_name = models.JSONField(blank=True, null=True)
    old_full_name_count = models.IntegerField(blank=True, null=True)
    old_username = models.JSONField(blank=True, null=True)
    old_username_count = models.IntegerField(blank=True, null=True)
    old_phone = models.JSONField(blank=True, null=True)
    old_phone_count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tg_group_user'


class TgTopic(models.Model):
    tg_topic_id = models.IntegerField(blank=True, null=True)
    tg_group = models.ForeignKey(TgGroup, models.DO_NOTHING, blank=True, null=True)
    created_time = models.DateTimeField(blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    topic_creator_id = models.BigIntegerField(blank=True, null=True)
    notify_settings = models.JSONField(blank=True, null=True)
    closed = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tg_topic'


class TgUser(models.Model):
    tg_id = models.BigIntegerField()
    first_name = models.CharField(max_length=255, blank=True, null=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    status = models.JSONField(blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    photo = models.JSONField(blank=True, null=True)
    mtproto = models.JSONField(blank=True, null=True)
    bot = models.BooleanField(blank=True, null=True)
    old_first_name = models.JSONField(blank=True, null=True)
    old_first_name_count = models.IntegerField(blank=True, null=True)
    old_username = models.JSONField(blank=True, null=True)
    old_phone = models.JSONField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tg_user'


class User(models.Model):
    user_id = models.BigIntegerField()
    username = models.CharField(max_length=255, blank=True, null=True)
    fullname = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'
