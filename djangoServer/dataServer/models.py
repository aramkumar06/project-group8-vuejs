# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Youtuber(models.Model):
    yno = models.AutoField(primary_key=True)
    channelid = models.CharField(db_column='channelID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    channelname = models.CharField(db_column='channelName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    youtubername = models.CharField(db_column='youtuberName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    channeldescription = models.CharField(db_column='channelDescription', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    bannerimagelink = models.CharField(db_column='bannerImageLink', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    channellink = models.CharField(db_column='channelLink', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    thumbnails = models.CharField(max_length=1000, blank=True, null=True)
    publisheddate = models.DateField(db_column='publishedDate', blank=True, null=True)  # Field name made lowercase.
    subscriber = models.IntegerField(blank=True, null=True)
    totalviewcount = models.BigIntegerField(db_column='totalViewCount', blank=True, null=True)  # Field name made lowercase.
    totalvideocount = models.IntegerField(db_column='totalVideoCount', blank=True, null=True)  # Field name made lowercase.
    grade = models.CharField(max_length=10, blank=True, null=True)
    influence = models.IntegerField(blank=True, null=True)
    activity = models.IntegerField(blank=True, null=True)
    growth = models.IntegerField(blank=True, null=True)
    basicstat = models.IntegerField(db_column='basicStat', blank=True, null=True)  # Field name made lowercase.
    charm = models.IntegerField(blank=True, null=True)
    clickcount = models.IntegerField(db_column='clickCount', blank=True, null=True)  # Field name made lowercase.
    updateddate = models.DateTimeField(db_column='updatedDate', blank=True, null=True)  # Field name made lowercase.
    regdate = models.DateField(db_column='regDate', blank=True, null=True)  # Field name made lowercase.
    otherlink1 = models.CharField(db_column='otherLink1', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    otherlink2 = models.CharField(db_column='otherLink2', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    otherlink3 = models.CharField(db_column='otherLink3', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    otherlink4 = models.CharField(db_column='otherLink4', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    otherlink5 = models.CharField(db_column='otherLink5', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    uploadsid = models.CharField(db_column='uploadsID', max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'youtuber'

    def __str__(self):
        return self.yno

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
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
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Category(models.Model):
    cano = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    clickcount = models.IntegerField(db_column='clickCount', blank=True, null=True)  # Field name made lowercase.
    imagelink = models.CharField(db_column='imageLink', max_length=1000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'category'


class CategoryYoutubeRelation(models.Model):
    yno = models.ForeignKey(Youtuber, models.DO_NOTHING, db_column='yno')
    cano = models.ForeignKey(Category, models.DO_NOTHING, db_column='cano')

    class Meta:
        managed = False
        db_table = 'category_youtube_relation'
        unique_together = (('yno', 'cano'),)


class Community(models.Model):
    cono = models.AutoField(primary_key=True)
    communityname = models.CharField(db_column='communityName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    communityagegroup = models.CharField(db_column='communityAgeGroup', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'community'


class CommunityYoutuberRelation(models.Model):
    yno = models.ForeignKey(Youtuber, models.DO_NOTHING, db_column='yno')
    cono = models.ForeignKey(Community, models.DO_NOTHING, db_column='cono')
    mentioncount = models.IntegerField(db_column='mentionCount', blank=True, null=True)  # Field name made lowercase.
    updatedate = models.DateTimeField(db_column='updateDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'community_youtuber_relation'
        unique_together = (('yno', 'cono'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
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


class Growth(models.Model):
    gno = models.AutoField(primary_key=True)
    yno = models.ForeignKey(Youtuber, models.DO_NOTHING, db_column='yno', related_name="youtuber_growth")
    recorddate = models.DateTimeField(db_column='recordDate', blank=True, null=True)  # Field name made lowercase.
    pointsubscriber = models.IntegerField(db_column='pointSubscriber', blank=True, null=True)  # Field name made lowercase.
    difsubscriber = models.IntegerField(db_column='difSubscriber', blank=True, null=True)  # Field name made lowercase.
    pointview = models.BigIntegerField(db_column='pointView', blank=True, null=True)  # Field name made lowercase.
    difview = models.IntegerField(db_column='difView', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'growth'


class News(models.Model):
    nno = models.AutoField(primary_key=True)
    yno = models.ForeignKey(Youtuber, models.DO_NOTHING, db_column='yno')
    newslink = models.CharField(db_column='newsLink', max_length=100, blank=True, null=True)  # Field name made lowercase.
    newstitle = models.CharField(db_column='newsTitle', max_length=100, blank=True, null=True)  # Field name made lowercase.
    newsdescription = models.CharField(db_column='newsDescription', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    newsdate = models.DateField(db_column='newsDate', blank=True, null=True)  # Field name made lowercase.
    pressname = models.CharField(db_column='pressName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    clickcount = models.IntegerField(db_column='clickCount', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'news'


class Video(models.Model):
    vno = models.AutoField(primary_key=True)
    yno = models.ForeignKey(Youtuber, models.DO_NOTHING, db_column='yno')
    videoid = models.CharField(db_column='videoID', max_length=100)  # Field name made lowercase.
    videoname = models.CharField(db_column='videoName', max_length=100)  # Field name made lowercase.
    videodescription = models.CharField(db_column='videoDescription', max_length=3000, blank=True, null=True)  # Field name made lowercase.
    videoviewcount = models.IntegerField(db_column='videoViewCount')  # Field name made lowercase.
    videocommentcount = models.IntegerField(db_column='videoCommentCount')  # Field name made lowercase.
    good = models.IntegerField()
    bad = models.IntegerField()
    regdate = models.DateField(db_column='regDate')  # Field name made lowercase.
    ycano = models.IntegerField(blank=True, null=True)
    tags = models.CharField(max_length=1000, blank=True, null=True)
    thumbnail = models.CharField(max_length=1000)
    topic = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'video'


class YoutubeCategory(models.Model):
    ycano = models.IntegerField(primary_key=True)
    encategory = models.CharField(db_column='enCategory', max_length=30)  # Field name made lowercase.
    krcategory = models.CharField(db_column='krCategory', max_length=30)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'youtube_category'



