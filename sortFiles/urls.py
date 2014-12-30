from django.conf.urls import patterns, url
from sortFiles import views

urlpatterns = patterns('',
    url(r'^$',views.index, name='index'),
    url(r'^mp3TorrentList',views.mp3TorrentList, name='mp3TorrentList'),
    url(r'^showList',views.showList, name='showList')
)