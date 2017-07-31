# encoding:utf-8

from django.conf.urls import url
from alonewell import views

urlpatterns = [
    url(r'addwell$', views.addwell, name='addwell'),
    url(r'query_well$', views.query_well, name='query_well'),
    url(r'query_well/(\d+)/$', views.query_well_del, name='query_well_del'),
    url(r'add_operate_parameters$', views.add_operate_parameters,
        name='add_operate_parameters'),
    url(r'add_operate_parameters/(\d+)/$',views.query_parameters_del,name='query_parameters_del'),
    url(r'well_status$',views.well_status,name='well_status'),
    url(r'well_technique$',views.well_technique,name='well_technique'),
    url(r'isvalid_wellNo$', views.isvalid_wellNo, name='isvalid_wellNo'),
    url(r'query_parameters', views.query_parameters,name='query_parameters'),
    url(r'shift_work_report', views.shift_work_report,name='shift_work_report'),
    url(r'daily_work_report', views.daily_work_report,name='daily_work_report'),
    url(r'test$', views.test, name='test'),
    url(r'test01$', views.test01, name='test01'),

]
