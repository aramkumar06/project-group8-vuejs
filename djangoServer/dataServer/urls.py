from django.urls import path
from . import views

urlpatterns = [
    path('updateStat', views.update_stat_all),
    path('newYoutuber/<str:url>', views.make_new_youtuber),
    path('ynoFromUrl/<str:url>', views.yno_from_url),
    path('statusFromYno/<int:yno>', views.status_from_yno),
]
