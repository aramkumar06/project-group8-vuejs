# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

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
    clickcount = models.IntegerField(db_column='clickCount', blank=True, null=True)
    imagelink = models.CharField(db_column='imageLink', max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'category'

    def __str__(self):
        return self.name


class CategoryYoutubeRelation(models.Model):
    cyno = models.AutoField(primary_key=True)
    yno = models.ForeignKey('Youtuber', models.DO_NOTHING, db_column='yno')
    cano = models.ForeignKey(Category, models.DO_NOTHING, db_column='cano')

    class Meta:
        managed = False
        db_table = 'category_youtube_relation'


class Community(models.Model):
    cono = models.AutoField(primary_key=True)
    yno = models.ForeignKey('Youtuber', models.DO_NOTHING, db_column='yno')
    articletitle = models.CharField(db_column='articleTitle', max_length=100, blank=True, null=True)
    articlelink = models.CharField(db_column='articleLink', max_length=1000, blank=True, null=True)
    articledescription = models.CharField(db_column='articleDescription', max_length=300, blank=True, null=True)
    articledate = models.DateField(db_column='articleDate', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'community'

    def __str__(self):
        return self.articletitle


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


class Favorite(models.Model):
    yno = models.IntegerField(primary_key=True)
    usno = models.IntegerField()
    regdate = models.DateField(db_column='regDate', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'favorite'
        unique_together = (('yno', 'usno'),)


class Interest(models.Model):
    itno = models.IntegerField(primary_key=True)
    itname = models.CharField(db_column='itName', max_length=50)  

    class Meta:
        managed = False
        db_table = 'interest'


class InterestUserRelation(models.Model):
    usno = models.ForeignKey('User', models.DO_NOTHING, db_column='usno', primary_key=True)
    itno = models.ForeignKey(Interest, models.DO_NOTHING, db_column='itno')

    class Meta:
        managed = False
        db_table = 'interest_user_relation'
        unique_together = (('usno', 'itno'),)


class Naverdatalab(models.Model):
    dno = models.AutoField(primary_key=True)
    yno = models.ForeignKey('Youtuber', models.DO_NOTHING, db_column='yno', blank=True, null=True)
    searchkeyword = models.CharField(db_column='searchKeyword', max_length=100, blank=True, null=True)
    startdate = models.DateField(db_column='startDate', blank=True, null=True)
    enddate = models.DateField(db_column='endDate', blank=True, null=True)
    data = models.CharField(max_length=16000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'naver_data_lab'


class News(models.Model):
    nno = models.AutoField(primary_key=True)
    yno = models.ForeignKey('Youtuber', models.DO_NOTHING, db_column='yno')
    newslink = models.CharField(db_column='newsLink', max_length=100, blank=True, null=True)
    newstitle = models.CharField(db_column='newsTitle', max_length=100, blank=True, null=True)
    newsdescription = models.CharField(db_column='newsDescription', max_length=1000, blank=True, null=True)
    newsdate = models.DateField(db_column='newsDate', blank=True, null=True)
    pressname = models.CharField(db_column='pressName', max_length=50, blank=True, null=True)
    clickcount = models.IntegerField(db_column='clickCount', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'news'

    def __str__(self):
        return self.newstitle


class Stat(models.Model):
    sno = models.AutoField(primary_key=True)
    yno = models.ForeignKey('Youtuber', models.DO_NOTHING, db_column='yno')
    kinds = models.IntegerField(db_column='kinds', blank=True, null=True)
    value = models.FloatField(db_column='value', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stat'


class TempMonth(models.Model):
    month_date = models.DateField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'temp_month'


class TempWeek(models.Model):
    week_lastday = models.DateField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'temp_week'


class Trend(models.Model):
    tno = models.AutoField(primary_key=True)
    yno = models.ForeignKey('Youtuber', models.DO_NOTHING, db_column='yno')
    recorddate = models.DateTimeField(db_column='recordDate', blank=True, null=True)
    pointsubscriber = models.IntegerField(db_column='pointSubscriber', blank=True, null=True)
    difsubscriber = models.IntegerField(db_column='difSubscriber', blank=True, null=True)
    pointview = models.BigIntegerField(db_column='pointView', blank=True, null=True)
    difview = models.IntegerField(db_column='difView', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trend'


class User(models.Model):
    usno = models.AutoField(primary_key=True)
    userid = models.CharField(db_column='userID', max_length=100)
    useremail = models.CharField(db_column='userEmail', max_length=100, blank=True, null=True)
    username = models.CharField(db_column='userName', max_length=100)
    regdate = models.DateField(db_column='regDate')

    class Meta:
        managed = False
        db_table = 'user'


class Video(models.Model):
    vno = models.AutoField(primary_key=True)
    yno = models.ForeignKey('Youtuber', models.DO_NOTHING, db_column='yno')
    videoid = models.CharField(db_column='videoID', max_length=100)  
    videoname = models.CharField(db_column='videoName', max_length=100)  
    videodescription = models.CharField(db_column='videoDescription', max_length=10000, blank=True, null=True)  
    videoviewcount = models.IntegerField(db_column='videoViewCount')  
    videocommentcount = models.IntegerField(db_column='videoCommentCount')  
    good = models.IntegerField()
    bad = models.IntegerField()
    regdate = models.DateField(db_column='regDate')  
    ycano = models.IntegerField(blank=True, null=True)
    tags = models.CharField(max_length=1000, blank=True, null=True)
    thumbnail = models.CharField(max_length=1000)
    topic = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'video'

    def __str__(self):
        return self.videoname


class YoutubeCategory(models.Model):
    ycano = models.IntegerField(primary_key=True)
    encategory = models.CharField(db_column='enCategory', max_length=30)
    krcategory = models.CharField(db_column='krCategory', max_length=30)

    class Meta:
        managed = False
        db_table = 'youtube_category'


class Youtuber(models.Model):
    yno = models.AutoField(primary_key=True)
    channelid = models.CharField(db_column='channelID', max_length=100, blank=True, null=True)
    channelname = models.CharField(db_column='channelName', max_length=100, blank=True, null=True)
    youtubername = models.CharField(db_column='youtuberName', max_length=100, blank=True, null=True)
    channeldescription = models.CharField(db_column='channelDescription', max_length=1000, blank=True, null=True)
    bannerimagelink = models.CharField(db_column='bannerImageLink', max_length=1000, blank=True, null=True)
    channellink = models.CharField(db_column='channelLink', max_length=1000, blank=True, null=True)
    thumbnails = models.CharField(max_length=1000, blank=True, null=True)
    publisheddate = models.DateField(db_column='publishedDate', blank=True, null=True)
    subscriber = models.IntegerField(blank=True, null=True)
    totalviewcount = models.BigIntegerField(db_column='totalViewCount', blank=True, null=True)
    totalvideocount = models.IntegerField(db_column='totalVideoCount', blank=True, null=True)
    grade = models.IntegerField(blank=True, null=True)
    influence = models.IntegerField(blank=True, null=True)
    activity = models.IntegerField(blank=True, null=True)
    viewcounttrend = models.IntegerField(db_column='viewCountTrend', blank=True, null=True)
    subscribercounttrend = models.IntegerField(db_column='subscriberCountTrend', blank=True, null=True)
    charm = models.IntegerField(blank=True, null=True)
    clickcount = models.IntegerField(db_column='clickCount', blank=True, null=True)
    updateddate = models.DateTimeField(db_column='updatedDate', blank=True, null=True)
    regdate = models.DateField(db_column='regDate', blank=True, null=True)
    otherlink1 = models.CharField(db_column='otherLink1', max_length=1000, blank=True, null=True)
    otherlink2 = models.CharField(db_column='otherLink2', max_length=1000, blank=True, null=True)
    otherlink3 = models.CharField(db_column='otherLink3', max_length=1000, blank=True, null=True)
    otherlink4 = models.CharField(db_column='otherLink4', max_length=1000, blank=True, null=True)
    otherlink5 = models.CharField(db_column='otherLink5', max_length=1000, blank=True, null=True)
    uploadsid = models.CharField(db_column='uploadsID', max_length=100, blank=True, null=True)
    searchkeyword = models.CharField(db_column='searchKeyword', max_length=100, blank=True, null=True)
    status = models.IntegerField(db_column='status', blank=True, null=True)
    tagcloud = models.CharField(max_length=7000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'youtuber'

    def __str__(self):
        return self.channelname