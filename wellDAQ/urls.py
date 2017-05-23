# encoding:utf-8

"""wellDAQ URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from wellDAQ import views
# from TestModel import views as TestModel_views
#
router = routers.DefaultRouter()
router.register(r'data', views.WellBasicDataViewSet)
router.register(r'parameter', views.OperateParametersViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # 测试用的url
    # url(r'^index/$', TestModel_views.index),
    # url(r'^home/$', TestModel_views.home),
    # url(r'^home2/$', TestModel_views.home2),
    # url(r'^add/$', TestModel_views.add, name='add'),

    # url(r'^index2/$', TestModel_views.index2, name='form'),

    # url(r'^add/(\d+)/(\d+)/$', TestModel_views.add2, name='add2'),
    # url(r'^login/$', TestModel_views.login, name='login'),
    # url(r'^ajax/$', TestModel_views.ajax, name='ajax'),
    # url(r'^ajax_dict/$', TestModel_views.ajax_dict, name='ajax-dict'),
    # url(r'^ajax_add/$', TestModel_views.ajax_add, name='ajax_add'),

    url(r'^', include('accounts.urls', namespace='accounts')),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^alonewell/', include('alonewell.urls', namespace='alonewell')),

]
