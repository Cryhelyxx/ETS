# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django import forms

from models import User
from account_md5 import md5
from mailer import send_email

# Create your views here.
def login(req):
    if req.method == 'POST':
        # username = req.GET.get('username')
        username = req.POST.get('username')
        password = req.POST.get('password')
        password = md5(password)
        user = User.objects.filter(username__exact = username, password__exact = password)
        if user:
            response = HttpResponseRedirect('/account/index/')
            response.set_cookie('username', username, 3600)
            return response
        else:
            return HttpResponseRedirect('/account/signin/')
    return render_to_response('signin.html', None, context_instance=RequestContext(req))

# 登录成功
def index(req):
    username = req.COOKIES.get('username', '')
    return render_to_response('index.html', {'username': username})

# 注册
def register(req):
    if req.method == 'POST':
        username = req.POST.get('username')
        password = req.POST.get('password')
        print username
        print password
        password = md5(password)
        user = User.objects.filter(username__exact = username, password__exact = password)
        # 如果用户已存在
        if user:
            return HttpResponse('用户已存在， 请直接登录')
        # 插入到数据库
        User.objects.create(username = username, password = password)
        send_email()
        return HttpResponse('注册成功！')
    return render_to_response('signup.html', None, context_instance=RequestContext(req))

# 注销
def logout(req):
    response = HttpResponse('注销成功!')
    # 清理cookie里保存的username
    response.delete_cookie('username')
    return response


