# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from account import views

urlpatterns = patterns('',
    url(r'^$', views.login, name="signin"),
    url(r'^signin/$', views.login, name="login"),
    url(r'^index/$', views.index, name="index"),
    url(r'^signup/$', views.register, name="signup"),

)
