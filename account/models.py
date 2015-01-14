# -*- coding: utf-8 -*-

from django.db import models
from django.contrib import admin

# Create your models here.
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(null=False, max_length=50)
    email = models.CharField(null=False, max_length=100)
    password = models.CharField(null=False, max_length=50)
    birthday = models.DateField(null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)




