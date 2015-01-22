# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import time
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect

from models import MyUser
from account_md5 import md5
from mailer import send_email

# Create your views here.
@login_required(login_url='/account/signin/')
def home(request):
    if request.user.is_authenticated():
        # Do something for authenticated users.
        return render(request, 'index.html')
    else:
        # Do something for anonymous users.
        return HttpResponse('禁用的账户')

def login_view(request):
    if request.method == 'POST':
        # username = request.GET.get('username')
        # username = request.POST.get('username')
        username = request.POST['username']
        password = request.POST['password']
        # user = User.objects.filter(username__exact = username, password__exact = password)
        user = authenticate(username = username, password = password)
        if user:
            if user.is_active:
                login(request, user)
                # Redirect to a success page.
                # return render(request, 'index.html')
                return redirect('/')
            else:
                # Return a 'disable account' error message.
                return HttpResponse('禁用的账户')
        else:
            # Return an 'invalid login' error message.
            return redirect('/account/signin/')
        
    return render(request, 'signin.html')


# 注册
def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        print username
        print password
        print email
        # user1 = User.objects.get(username__exact = username)
        # user2 = User.objects.get(email = email)
        # 执行原生查询并返回模型实例
        # raw_sql = 'select * from account_user u where u.username = %s' % username
        #user1 = User.objects.raw(raw_sql)
        #raw_sql = 'select * from account_user u where u.email = %s' % email
        #user2 = User.objects.raw(raw_sql)
        user1 = User.objects.filter(username=username)
        user2 = User.objects.filter(email=email)
        # 如果用户已存在
        if user1:
            msg = '用户名 %s 已存在， 请重试！' %  username
            return HttpResponse(msg)
        elif user2:
            msg = '邮箱 %s 已存在， 请重试！' % email
            return HttpResponse(msg)
        else:
            # 插入到数据库
            user = User.objects.create_user(username, email, password)
            user.is_active = True
            user.save()
            send_email(email, username)
            return HttpResponse('注册成功！')
    else:
        return render(request, 'signup.html')


def logout_view(request):
    logout(request)
    # Redirect to a success page.
    return redirect('/')



