from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

import core.views

urlpatterns = patterns('',
    url(r'^$', core.views.index),
    url(r'^(?P<tweets_id>[,?\w]+)/$', core.views.get_tweets, name='index'),
)
