# encoding:utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.

# 基础的单井数据表


class WellBasicData(models.Model):

    class Meta:
        # 权限设置
        permissions = (
            ('test1_wellbasicdata', 'this is test for permissions'),
            ('test2_wellbasicdata', 'this is test for permissions'),
            ('test3_wellbasicdata', 'this is test for permissions'),
        )
    wellNo = models.IntegerField(primary_key=True)
    wellName = models.CharField(max_length=40)
    dimension = models.FloatField()  # 维度
    longitude = models.FloatField()  # 经度

    def __unicode__(self):
        return self.wellName

# 单井采集的数据


class OperateParameters(models.Model):
    wellNo = models.ForeignKey(WellBasicData, related_name='wellmodel')
    data_storage = models.DateTimeField(blank=True)
    targetpress = models.FloatField(blank=True)
    presentpress = models.FloatField(blank=True)
    bottompress = models.FloatField(blank=True)
    targetflow = models.IntegerField(blank=True)
    presentflow = models.IntegerField(blank=True)
    totalflow = models.IntegerField(blank=True)
    dailyflow = models.IntegerField(blank=True)
    cycle = models.IntegerField(blank=True)
    stepRange = models.FloatField(blank=True)
    instantLP = models.FloatField(blank=True)
    totalLP = models.FloatField(blank=True)
    valvelift = models.IntegerField(blank=True)

    def __unicode__(self):
        return self.wellNo.wellName
