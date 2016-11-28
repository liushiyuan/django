"""wechat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^api/admin/', include(admin.site.urls)),
    url(r'^api/post/', 'eqshow.views.doPost'),
    url(r'^api/youtube/post', 'youtube.views.doPost'),
    url(r'^api/verycd/post', 'verycd.views.doPost'),
    url(r'^api/google/post', 'google.views.doPost'),
    url(r'^api/bt/post', 'bt.views.doPost'),
    url(r'^api/movie/list/(?P<page>\d+)$', 'movie.views.getList'),
    url(r'^api/movie/id/(?P<name>.+)$', 'movie.views.getMovieDes'),
    url(r'^api/movie/tv/(?P<name>.+)$', 'movie.views.getTvDes'),
    url(r'^api/movie/key/(?P<name>[^/]+)$', 'movie.views.searchMovieList'),
    url(r'^api/movie/key/(?P<name>[^/]+)/(?P<page>\d+)$', 'movie.views.searchMovieList'),
    url(r'^api/movie/tag/(?P<name>[^/]+)$', 'movie.views.tagMovieList'),
    url(r'^api/movie/tag/(?P<name>[^/]+)/$', 'movie.views.tagMovieList'),
    url(r'^api/movie/tag/(?P<name>[^/]+)/(?P<page>\d+)$', 'movie.views.tagMovieList'),
]
