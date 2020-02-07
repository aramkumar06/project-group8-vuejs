from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('newYoutuber/<str:url>', views.make_new_youtuber),
    path('updateYoutuber/<int:yno>', views.update_youtuber),
]
