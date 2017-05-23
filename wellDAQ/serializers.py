# encoding:utf-8
from rest_framework import serializers
from alonewell.models import WellBasicData, OperateParameters


class WellBasicDataSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = WellBasicData
        fields = ('wellNo', 'wellName', 'dimension', 'longitude')


class OperateParametersSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = OperateParameters
        fields = ('wellNo', 'data_storage', 'targetpress', 'presentpress',
                  'bottompress', 'targetflow', 'presentflow', 'totalflow')
