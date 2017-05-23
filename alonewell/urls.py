# encoding:utf-8

from django.conf.urls import url
from alonewell import views

urlpatterns = [
    url(r'addwell$', views.addwell, name='addwell'),
    url(r'query_well$', views.query_well, name='query_well'),
    url(r'add_operate_parameters$', views.add_operate_parameters,
        name='add_operate_parameters'),
    url(r'isvalid_wellNo$', views.isvalid_wellNo, name='isvalid_wellNo'),
    url(r'test$', views.test, name='test'),
    url(r'test01$', views.test01, name='test01'),

]
