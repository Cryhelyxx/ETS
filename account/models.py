# -*- coding: utf-8 -*-

from django.db import models
from django.contrib import admin
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser, PermissionsMixin)
# from django.contrib.sites.models import Site

# Create your models here.
class UserManager(BaseUserManager):
    '''
        用户管理表
        UserManager class继续BaseUserManager
    
    '''
    def create_user(self, username, email, password=None):
        ''' 创建用户'''
        
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            username = username,
            email = UserManager.normalize_email(email),
        )

        user.set_password(password)
        user.save(using = self._db)
        return user


    def create_superuser(self, username, email, password=None):
        ''' 创建超级用户 '''
        
        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.save(using = self._db)
        return user



class MyUser(AbstractBaseUser, PermissionsMixin):
    ''' 
        用户表
        User class继续AbstractBaseUser
    '''
    # id = models.AutoField(primary_key=True)
    username = models.CharField(null=False, max_length=50, unique=True)
    email = models.EmailField(
        verbose_name = 'email address',
        max_length = 255,
        unique = True
    )
    avatar = models.URLField(blank=True)
    nickname = models.CharField(null=True, max_length=50, blank=True)
    realname = models.CharField(null=True, max_length=50, blank=True)
    qq = models.CharField(null=True, max_length=50, blank=True)
    weixin = models.CharField(null=True, max_length=100, blank=True)
    mobilephone = models.CharField(null=True, max_length=20, blank=True)
    certificate = models.CharField(null=True, max_length=100, blank=True)
    address = models.CharField(null=True, max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_delete = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    # is_admin = models.BooleanField(default=False)
    is_lock = models.BooleanField(default=False)
    access_token = models.CharField(max_length=100, blank=True)
    refresh_token = models.CharField(max_length=100, blank=True)
    expires_in = models.BigIntegerField(max_length=100, default=0)
    
    # groups = models.ManyToManyField(Group)
    # user_permissions = models.ManyToManyField(Permission)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ('email',)

    class Meta:
        ordering = ('-created_at',)

    def __unicode__(self):
        return self.username

    ''' get_short_name,get_full_name需要实现,否则会抛异常, 查看AbstractBaseUser源码可知 '''
    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.is_superuser



