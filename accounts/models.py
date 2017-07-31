# encoding:utf-8
from __future__ import unicode_literals
from django.contrib.auth.models import User

from django.db import models

# Create your models here.

# 用户详细信息
class UserProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, unique=True)
    true_name = models.CharField(max_length=40)
    department = models.CharField(max_length=40)
    position = models.CharField(max_length=40)

# 部门
class Department(models.Model):
    department_name = models.CharField(max_length=40)

# 职位
class Position(models.Model):
    position_name = models.CharField(max_length=40)
    department=models.ForeignKey(Department)
