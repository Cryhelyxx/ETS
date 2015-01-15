# -*- coding: utf-8 -*-

from django.db import models
from django.contrib import admin

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(null=False, max_length=50, unique=True)
    email = models.CharField(null=False, max_length=100, unique=True)
    password = models.CharField(null=False, max_length=50)
    avatar = models.URLField(blank=True)
    birthday = models.DateField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_lock = models.BooleanField(default=False)
    access_token = models.CharField(max_length=100, blank=True)
    refresh_token = models.CharField(max_length=100, blank=True)
    expires_in = models.BigIntegerField(max_length=100, default=0)




