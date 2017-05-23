# encoding:utf-8

from rest_framework import viewsets
from alonewell.models import WellBasicData, OperateParameters
from wellDAQ.serializers import WellBasicDataSerializer, OperateParametersSerializer


class WellBasicDataViewSet(viewsets.ModelViewSet):
    queryset = WellBasicData.objects.all()
    serializer_class = WellBasicDataSerializer


class OperateParametersViewSet(viewsets.ModelViewSet):
    queryset = OperateParameters.objects.all()
    serializer_class = OperateParametersSerializer
