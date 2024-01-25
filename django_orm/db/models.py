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
    keyword_id = models.IntegerField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    files = models.CharField(max_length=255, blank=True, null=True)
    user_id = models.BigIntegerField(blank=True, null=True)
    peer_id = models.BigIntegerField(blank=True, null=True)
    message_full_link = models.CharField(max_length=255, blank=True, null=True)
    public_chat_link = models.CharField(max_length=255, blank=True, null=True)
    private_chat_link = models.CharField(max_length=255, blank=True, null=True)
    user_link = models.CharField(max_length=255, blank=True, null=True)
    msg_id_field = models.IntegerField(db_column='msg_id ', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    message_public_link = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'message'


class Rating(models.Model):

    datetime = models.DateTimeField(blank=True, null=True)
    report_id = models.IntegerField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    files = models.CharField(max_length=255, blank=True, null=True)
    user_id = models.BigIntegerField(blank=True, null=True)
    peer_id = models.BigIntegerField(blank=True, null=True)
    message_full_link = models.CharField(max_length=255, blank=True, null=True)
    public_chat_link = models.CharField(max_length=255, blank=True, null=True)
    private_chat_link = models.CharField(max_length=255, blank=True, null=True)
    user_link = models.CharField(max_length=255, blank=True, null=True)
    msg_id_field = models.IntegerField(db_column='msg_id ', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    message_public_link = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rating'


class Report(models.Model):

    link = models.CharField(max_length=255)
    topic_id = models.IntegerField(blank=True, null=True)
    message_id = models.IntegerField(blank=True, null=True)
    chat_id = models.IntegerField(blank=True, null=True)

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
    read_inbox_max_id = models.CharField(max_length=255, blank=True, null=True)
    read_outbox_max_id = models.CharField(max_length=255, blank=True, null=True)
    hidden_prehistory = models.CharField(max_length=255, blank=True, null=True)
    bot_info = models.TextField(blank=True, null=True)
    notify_settings = models.TextField(blank=True, null=True)
    can_set_stickers = models.CharField(max_length=255, blank=True, null=True)
    can_view_participants = models.CharField(max_length=255, blank=True, null=True)
    can_set_username = models.CharField(max_length=255, blank=True, null=True)
    participants_count = models.CharField(max_length=255, blank=True, null=True)
    admins_count = models.CharField(max_length=255, blank=True, null=True)
    kicked_count = models.CharField(max_length=255, blank=True, null=True)
    banned_count = models.CharField(max_length=255, blank=True, null=True)
    migrated_from_chat_id = models.CharField(max_length=255, blank=True, null=True)
    migrated_from_max_id = models.CharField(max_length=255, blank=True, null=True)
    pinned_msg_id = models.CharField(max_length=255, blank=True, null=True)
    about = models.CharField(max_length=255, blank=True, null=True)
    can_view_stats = models.CharField(max_length=255, blank=True, null=True)
    online_count = models.CharField(max_length=255, blank=True, null=True)
    invite = models.CharField(max_length=255, blank=True, null=True)
    participants = models.TextField(blank=True, null=True)
    mtproto = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    hrm_project_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tg_channel'


class TgChannelText(models.Model):
    type = models.CharField(max_length=255, blank=True, null=True, db_comment="qaysi turdigi xabarligi, (message, messageService). messageService bu kanal nomi o'zgarishi, kanal profili o'zgartirilishiga o'xshagan xabarla")
    creator_id = models.IntegerField(blank=True, null=True)
    performers_id = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    history = models.TextField(blank=True, null=True)
    full_url = models.CharField(max_length=255, blank=True, null=True)
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
    tg_channel_id = models.IntegerField(blank=True, null=True)
    tg_id = models.IntegerField(blank=True, null=True)
    from_id_field = models.CharField(db_column='from_id__', max_length=255, blank=True, null=True)  # Field renamed because it contained more than one '_' in a row. Field renamed because it ended with '_'.
    from_id_user_id = models.BinaryField(blank=True, null=True)
    peer_id_field = models.CharField(db_column='peer_id__', max_length=255, blank=True, null=True)  # Field renamed because it contained more than one '_' in a row. Field renamed because it ended with '_'.
    peer_id_channel_id = models.IntegerField(blank=True, null=True)
    fwd_from_field = models.CharField(db_column='fwd_from__', max_length=255, blank=True, null=True)  # Field renamed because it contained more than one '_' in a row. Field renamed because it ended with '_'.
    fwd_from_imported = models.SmallIntegerField(blank=True, null=True)
    fwd_from_from_id = models.TextField(blank=True, null=True)
    fwd_from_date = models.DateTimeField(blank=True, null=True)
    fwd_from_channel_post = models.IntegerField(blank=True, null=True)
    fwd_from_saved_from_peer = models.TextField(blank=True, null=True)
    fwd_from_saved_from_msg_id = models.IntegerField(blank=True, null=True)
    entities = models.TextField(blank=True, null=True)
    views = models.IntegerField(blank=True, null=True)
    reply_to_field = models.CharField(db_column='reply_to__', max_length=255, blank=True, null=True)  # Field renamed because it contained more than one '_' in a row. Field renamed because it ended with '_'.
    reply_to_reply_to_scheduled = models.SmallIntegerField(blank=True, null=True)
    reply_to_reply_to_msg_id = models.CharField(max_length=11, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    replies_field = models.CharField(db_column='replies__', max_length=255, blank=True, null=True)  # Field renamed because it contained more than one '_' in a row. Field renamed because it ended with '_'.
    replies_replies = models.IntegerField(blank=True, null=True)
    replies_comments = models.SmallIntegerField(blank=True, null=True)
    replies_replies_pts = models.IntegerField(blank=True, null=True)
    replies_max_id = models.IntegerField(blank=True, null=True)
    replies_read_max_id = models.IntegerField(blank=True, null=True)
    replies_channel_id = models.IntegerField(blank=True, null=True)
    to_id_field = models.CharField(db_column='to_id__', max_length=255, blank=True, null=True)  # Field renamed because it contained more than one '_' in a row. Field renamed because it ended with '_'.
    to_id_channel_id = models.IntegerField(blank=True, null=True)
    media_field = models.CharField(db_column='media__', max_length=255, blank=True, null=True)  # Field renamed because it contained more than one '_' in a row. Field renamed because it ended with '_'.
    media = models.TextField(blank=True, null=True)
    action_field = models.CharField(db_column='action__', max_length=255, blank=True, null=True)  # Field renamed because it contained more than one '_' in a row. Field renamed because it ended with '_'.
    action = models.TextField(blank=True, null=True)
    dl_file_path = models.CharField(max_length=255, blank=True, null=True)
    dl_file_size = models.FloatField(blank=True, null=True)
    dl_status = models.SmallIntegerField(blank=True, null=True)
    check_tagged_user = models.SmallIntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    mtproto = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tg_channel_text'


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
    read_inbox_max_id = models.CharField(max_length=255, blank=True, null=True)
    read_outbox_max_id = models.CharField(max_length=255, blank=True, null=True)
    hidden_prehistory = models.CharField(max_length=255, blank=True, null=True)
    bot_info = models.TextField(blank=True, null=True)
    notify_settings = models.TextField(blank=True, null=True)
    can_set_stickers = models.CharField(max_length=255, blank=True, null=True)
    can_view_participants = models.CharField(max_length=255, blank=True, null=True)
    can_set_username = models.CharField(max_length=255, blank=True, null=True)
    participants_count = models.CharField(max_length=255, blank=True, null=True)
    admins_count = models.CharField(max_length=255, blank=True, null=True)
    kicked_count = models.CharField(max_length=255, blank=True, null=True)
    banned_count = models.CharField(max_length=255, blank=True, null=True)
    migrated_from_chat_id = models.CharField(max_length=255, blank=True, null=True)
    migrated_from_max_id = models.CharField(max_length=255, blank=True, null=True)
    pinned_msg_id = models.CharField(max_length=255, blank=True, null=True)
    about = models.CharField(max_length=255, blank=True, null=True)
    can_view_stats = models.CharField(max_length=255, blank=True, null=True)
    online_count = models.CharField(max_length=255, blank=True, null=True)
    invite = models.CharField(max_length=255, blank=True, null=True)
    participants = models.TextField(blank=True, null=True)
    mtproto = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    hrm_project_id = models.IntegerField(blank=True, null=True)
    is_active = models.BooleanField(blank=True, null=True)
    name_history = models.JSONField(blank=True, null=True)
    last_message_id = models.BigIntegerField(blank=True, null=True)
    days_count = models.SmallIntegerField(blank=True, null=True)

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
    tg_group_id = models.IntegerField(blank=True, null=True)
    edit_date = models.DateTimeField(blank=True, null=True)
    message_private_link = models.CharField(unique=True, max_length=255)
    type = models.CharField(max_length=255, blank=True, null=True)
    pinned = models.BooleanField(blank=True, null=True)
    media = models.JSONField(blank=True, null=True)
    post = models.BooleanField(blank=True, null=True)
    out = models.BooleanField(blank=True, null=True)
    replies_count = models.IntegerField(blank=True, null=True)
    max_id = models.IntegerField(blank=True, null=True)
    read_max_id = models.IntegerField(blank=True, null=True)
    comments = models.BooleanField(blank=True, null=True)
    old_content = models.JSONField(blank=True, null=True)
    old_count = models.IntegerField(blank=True, null=True)
    message_public_link = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tg_group_message'


class TgGroupText(models.Model):

    type = models.CharField(max_length=255, blank=True, null=True)
    message_private_link = models.CharField(max_length=255, blank=True, null=True)
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
    from_id_field = models.CharField(db_column='from_id__', max_length=255, blank=True, null=True)  # Field renamed because it contained more than one '_' in a row. Field renamed because it ended with '_'.
    from_id_user_id = models.BinaryField(blank=True, null=True)
    peer_id_field = models.CharField(db_column='peer_id__', max_length=255, blank=True, null=True)  # Field renamed because it contained more than one '_' in a row. Field renamed because it ended with '_'.
    peer_id_channel_id = models.IntegerField(blank=True, null=True)
    fwd_from_field = models.CharField(db_column='fwd_from__', max_length=255, blank=True, null=True)  # Field renamed because it contained more than one '_' in a row. Field renamed because it ended with '_'.
    fwd_from_imported = models.SmallIntegerField(blank=True, null=True)
    fwd_from_from_id = models.TextField(blank=True, null=True)
    fwd_from_date = models.DateTimeField(blank=True, null=True)
    fwd_from_channel_post = models.IntegerField(blank=True, null=True)
    fwd_from_saved_from_peer = models.TextField(blank=True, null=True)
    fwd_from_saved_from_msg_id = models.IntegerField(blank=True, null=True)
    entities = models.TextField(blank=True, null=True)
    views = models.IntegerField(blank=True, null=True)
    reply_to_field = models.CharField(db_column='reply_to__', max_length=255, blank=True, null=True)  # Field renamed because it contained more than one '_' in a row. Field renamed because it ended with '_'.
    reply_to_reply_to_scheduled = models.SmallIntegerField(blank=True, null=True)
    reply_to_reply_to_msg_id = models.CharField(max_length=11, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    replies_field = models.CharField(db_column='replies__', max_length=255, blank=True, null=True)  # Field renamed because it contained more than one '_' in a row. Field renamed because it ended with '_'.
    replies_replies = models.IntegerField(blank=True, null=True)
    replies_comments = models.SmallIntegerField(blank=True, null=True)
    replies_replies_pts = models.IntegerField(blank=True, null=True)
    replies_max_id = models.IntegerField(blank=True, null=True)
    replies_read_max_id = models.IntegerField(blank=True, null=True)
    to_id_field = models.CharField(db_column='to_id__', max_length=255, blank=True, null=True)  # Field renamed because it contained more than one '_' in a row. Field renamed because it ended with '_'.
    to_id_channel_id = models.IntegerField(blank=True, null=True)
    media_field = models.CharField(db_column='media__', max_length=255, blank=True, null=True)  # Field renamed because it contained more than one '_' in a row. Field renamed because it ended with '_'.
    media = models.TextField(blank=True, null=True)
    action_field = models.CharField(db_column='action__', max_length=255, blank=True, null=True)  # Field renamed because it contained more than one '_' in a row. Field renamed because it ended with '_'.
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
    message_history = models.JSONField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tg_group_text'


class TgGroupUser(models.Model):
    contact = models.BooleanField(blank=True, null=True)
    bot = models.BooleanField(blank=True, null=True)
    tg_group_user_id = models.BigIntegerField(blank=True, null=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    photo_field = models.JSONField(db_column='photo ', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    status = models.JSONField(blank=True, null=True)
    mtproto = models.JSONField(blank=True, null=True)
    tg_group = models.ForeignKey(TgGroup, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tg_group_user'


class TgRole(models.Model):

    name = models.CharField(max_length=255, blank=True, null=True)
    display_name = models.CharField(max_length=255, blank=True, null=True)
    send_messages = models.SmallIntegerField(blank=True, null=True)
    send_media = models.SmallIntegerField(blank=True, null=True)
    send_stickers = models.SmallIntegerField(blank=True, null=True)
    send_gifs = models.SmallIntegerField(blank=True, null=True)
    send_game = models.SmallIntegerField(blank=True, null=True)
    send_inline = models.SmallIntegerField(blank=True, null=True)
    embed_links = models.SmallIntegerField(blank=True, null=True)
    send_polls = models.SmallIntegerField(blank=True, null=True)
    change_info = models.SmallIntegerField(blank=True, null=True)
    invite_users = models.SmallIntegerField(blank=True, null=True)
    ping_messages = models.SmallIntegerField(blank=True, null=True)
    until_date = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tg_role'


class TgTopic(models.Model):
    tg_topic_id = models.IntegerField(blank=True, null=True)
    tg_group = models.ForeignKey(TgGroup, models.DO_NOTHING, blank=True, null=True)
    created_time = models.DateTimeField(blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    topic_creater_id = models.BigIntegerField(blank=True, null=True)
    notify_settings = models.JSONField(blank=True, null=True)
    closed = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tg_topic'


class TgUser(models.Model):

    tg_id = models.BigIntegerField()
    tg_role_id = models.SmallIntegerField(blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    full_name = models.CharField(max_length=255, blank=True, null=True, db_comment='Pasport formatida')
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    status = models.JSONField(blank=True, null=True)
    access_hash = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    bot_nochats = models.BooleanField(blank=True, null=True)
    phone_calls_available = models.CharField(max_length=255, blank=True, null=True)
    phone_calls_private = models.CharField(max_length=255, blank=True, null=True)
    common_chats_count = models.IntegerField(blank=True, null=True)
    can_pin_message = models.BooleanField(blank=True, null=True)
    notify_settings = models.JSONField(blank=True, null=True)
    photo = models.JSONField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    mtproto = models.TextField(blank=True, null=True)
    main_user = models.SmallIntegerField(blank=True, null=True)
    bot = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tg_user'


class TgUserRole(models.Model):
    tg_user_id = models.IntegerField(blank=True, null=True)
    tg_role_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tg_user_role'


class TgUserText(models.Model):

    tg_id = models.IntegerField(blank=True, null=True)
    field_field = models.CharField(db_column='_', max_length=255, blank=True, null=True)  # Field renamed because it started with '_'. Field renamed because it ended with '_'.
    out = models.CharField(max_length=255, blank=True, null=True)
    mentioned = models.CharField(max_length=255, blank=True, null=True)
    media_unread = models.CharField(max_length=255, blank=True, null=True)
    silent = models.CharField(max_length=255, blank=True, null=True)
    post = models.CharField(max_length=255, blank=True, null=True)
    from_scheduled = models.CharField(max_length=255, blank=True, null=True)
    legacy = models.CharField(max_length=255, blank=True, null=True)
    edit_hide = models.CharField(max_length=255, blank=True, null=True)
    pinned = models.CharField(max_length=255, blank=True, null=True)
    noforwards = models.CharField(max_length=255, blank=True, null=True)
    peer_id_field = models.CharField(db_column='peer_id_', max_length=255, blank=True, null=True)  # Field renamed because it ended with '_'.
    peer_id_user_id = models.CharField(max_length=255, blank=True, null=True)
    from_id_field = models.CharField(db_column='from_id_', max_length=255, blank=True, null=True)  # Field renamed because it ended with '_'.
    from_id_user_id = models.CharField(db_column='from_id.user_id', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    reply_to_field = models.CharField(db_column='reply_to_', max_length=255, blank=True, null=True)  # Field renamed because it ended with '_'.
    reply_to_reply_to_scheduled = models.CharField(max_length=255, blank=True, null=True)
    reply_to_reply_to_msg_id = models.CharField(max_length=255, blank=True, null=True)
    date = models.CharField(max_length=255, blank=True, null=True)
    edit_date = models.CharField(max_length=255, blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    media = models.TextField(blank=True, null=True)
    media_field = models.CharField(db_column='media_', max_length=255, blank=True, null=True)  # Field renamed because it ended with '_'.
    mtproto = models.TextField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tg_user_text'


class User(models.Model):

    user_id = models.BigIntegerField()
    username = models.CharField(max_length=255, blank=True, null=True)
    fullname = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'
