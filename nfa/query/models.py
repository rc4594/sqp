# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Users(models.Model):
    user_id = models.CharField(max_length = 20, null = False, primary_key = True)
    name = models.CharField(max_length = 30, null = False)
    q_count = models.IntegerField(default = 0)
    a_count = models.IntegerField(default = 0)
    reputation = models.IntegerField(default = 0)

class Questions(models.Model):
    q_id = models.CharField(max_length = 20, null = False, primary_key = True)
    q_des = models.CharField(max_length = 1000, null = False)
    q_tag = models.CharField(max_length = 30, null = False)
    q_by = models.CharField(max_length = 30, null = False)
    q_upvotes = models.IntegerField(default = 0)
    q_views = models.IntegerField(default = 0)
    q_time = models.TimeField(auto_now_add = True)
    q_acount = models.IntegerField(default = 0)
    q_reports = models.IntegerField(default = 0)

class Answers(models.Model):
    a_id = models.CharField(max_length = 20, null = False, primary_key = True)
    a_qid = models.ForeignKey(Questions, on_delete = models.CASCADE)
    a_by = models.CharField(max_length = 30, null = False)
    a_content = models.CharField(max_length = 1000, null = False)
    a_upvotes = models.IntegerField(default = 0)
    a_time = models.TimeField(auto_now_add = True)

class Comment(models.Model):
    c_id = models.CharField(max_length = 20, null = False, primary_key = True)
    c_parID = models.CharField(max_length = 20, null = False)
    c_time = models.TimeField(auto_now_add = True)
    c_by = models.CharField(max_length = 30, null = False)
    c_content = models.CharField(max_length = 1000, null = False)

