# encoding:utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.

# 基础的单井数据表.


class WellBasicData(models.Model):
    wellNo = models.IntegerField(primary_key=True)
    wellName = models.CharField(max_length=40)
    dimension = models.FloatField()  # 维度
    longitude = models.FloatField()  # 经度

    def __unicode__(self):
        return self.wellName

# 单井采集的数据


class OperateParameters(models.Model):
    wellNo = models.ForeignKey(WellBasicData, related_name='No')
    data_storage = models.DateField()
    targetpress = models.FloatField()
    presentpress = models.FloatField()
    bottompress = models.FloatField()
    targetflow = models.IntegerField()
    presentflow = models.IntegerField()
    totalflow = models.IntegerField()
    dailyflow = models.IntegerField()
    cycle = models.IntegerField()
    stepRange = models.FloatField()
    instantLP = models.FloatField()
    totalLP = models.FloatField()
    valvelift = models.IntegerField()

    def __unicode__(self):
        return self.wellNo
