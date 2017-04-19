# encoding:utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.
# 建立数据表table


class Test(models.Model):
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    def __unicode__(self):
        return self.name
