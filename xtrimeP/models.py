# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Chats(models.Model):
    id = models.IntegerField(primary_key=True)
    chat_id = models.IntegerField(unique=True)
    type = models.CharField(max_length=255)
    title = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'chats'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Keyword(models.Model):
    name = models.CharField(max_length=255)
    last_checked = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'keyword'


class Message(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    datetime = models.DateField(blank=True, null=True)
    keyword = models.ForeignKey(Keyword, models.DO_NOTHING)
    content = models.TextField(blank=True, null=True)
    files = models.CharField(max_length=255, blank=True, null=True)
    from_field = models.ForeignKey('Users', models.DO_NOTHING, db_column='from_id', to_field='user_id', blank=True, null=True)  # Field renamed because it was a Python reserved word.
    peer = models.ForeignKey(Chats, models.DO_NOTHING, to_field='chat_id', blank=True, null=True)
    topic_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'message'


class TgGroupTexts(models.Model):
    id = models.IntegerField(primary_key=True)
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

    class Meta:
        managed = False
        db_table = 'tg_group_texts'


class Users(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField(unique=True)
    username = models.CharField(max_length=255)
    fullname = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'users'
