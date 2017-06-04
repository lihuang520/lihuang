#coding = utf-8
from __future__ import unicode_literals

from django.db import models
from django.contrib import admin
# Create your models here.

class User(models.Model):
	username = models.CharField(max_length=16,null=False)
	password = models.CharField(max_length=32,null=False)
	age = models.IntegerField()



admin.site.register(User)


