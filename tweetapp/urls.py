from django.urls import include
from django.conf.urls import url
from tweetapp import views

urlpatterns = [
    url(r'^hashtags/(?P<searchword>[0-32A-Za-z0-9\-_]+)/', views.getTweetsByHashtag, name='getTweetsByHashtag'),
    url(r'^users/(?P<user>[0-32A-Za-z0-9\-_]+)/', views.getTweetsByUser, name='getTweetsByUser'),
]