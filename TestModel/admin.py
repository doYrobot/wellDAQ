# encoding:utf-8
from django.contrib import admin
from TestModel.models import Test
# Register your models here.
# 启用后台管理我们创建的model
admin.site.register(Test)
