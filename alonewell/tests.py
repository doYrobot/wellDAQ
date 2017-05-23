# encoding:utf-8
# 测试单元
from django.test import TestCase
from django.test import client
from alonewell.forms import AddOperateParametersForm, AddWellForm
from alonewell.models import WellBasicData, OperateParameters


class AlonewellTestCase(TestCase):

    def setUp(self):
        pass

    def test_operateparameters_post(self):
        pass
