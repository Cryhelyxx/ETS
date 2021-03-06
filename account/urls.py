# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from account import views

urlpatterns = patterns('',
    url(r'^$', views.login_view, name="login"),
    url(r'^signin/$', views.login_view, name="signin"),
    url(r'^signup/$', views.register_view, name="signup"),
    url(r'^logout/$', views.logout_view, name="logout"),
)
