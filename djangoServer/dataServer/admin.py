from django.contrib import admin
from .models import (Category, CategoryYoutubeRelation, Community, 
                    Favorite, Interest, InterestUserRelation, 
                    Naverdatalab, News, Stat, TempMonth, TempWeek, 
                    Trend, User, Video, YoutubeCategory, Youtuber)


class CateogryAmdin(admin.ModelAdmin):
    list_display = ('cano', 'name', 'clickcount',)


class CommunityAdmin(admin.ModelAdmin):
    list_display = ('cono', 'yno', 'articletitle', 'articledate',)


class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('yno', 'usno', 'regdate',)


class InterestAdmin(admin.ModelAdmin):
    list_display = ('itno', 'itname',)


class NaverdatalabAdmin(admin.ModelAdmin):
    list_display = ('dno', 'yno', 'searchkeyword', 'enddate',)


class NewsAdmin(admin.ModelAdmin):
    list_display = ('nno', 'yno', 'newstitle', 'newsdate',)


class StatAdmin(admin.ModelAdmin):
    list_display = ('sno', 'yno', 'kinds', 'value')


class TrendAdmin(admin.ModelAdmin):
    list_display = ('tno', 'yno', 'recorddate', 'pointsubscriber', 'difsubscriber', 'pointview', 'difview',)


class UserAdmin(admin.ModelAdmin):
    list_display = ('usno', 'userid', 'useremail', 'username', 'regdate',)


class VideoAdmin(admin.ModelAdmin):
    list_display = ('vno', 'yno', 'videoname', 'videoid', 'regdate',)


class YoutuberAdmin(admin.ModelAdmin):
    list_display = ('yno', 'channelid', 'channelname', 'searchkeyword', 'updateddate', 'regdate', 'status',)


admin.site.register(Youtuber, YoutuberAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Trend, TrendAdmin)
admin.site.register(Stat, StatAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Naverdatalab, NaverdatalabAdmin)
admin.site.register(Interest, InterestAdmin)
admin.site.register(Favorite, FavoriteAdmin)
admin.site.register(Category, CateogryAmdin)
admin.site.register(Community, CommunityAdmin)
