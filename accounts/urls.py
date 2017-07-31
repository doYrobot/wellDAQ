# encoding:utf-8

from django.conf.urls import url
from accounts import views
# from django.contrib import admin


urlpatterns = [
    url(r'^$', views.mylogin, name='login'),
    url(r'signup$', views.signup, name='signup'),
    url(r'index$', views.index, name='index'),
    url(r'loginout$', views.loginout, name='loginout'),
    url(r'accounts/detail$', views.set_user_detail, name='set_user_detail'),
    url(r'accounts/set_permissions',views.set_user_permissions,name='set_permissions'),
    url(r'accounts/create_department',views.create_department,name='create_department'),
    url(r'accounts/create_position',views.create_position,name='create_position'),
    url(r'accounts/create_permissions',views.create_permissions,name='create_permissions'),
]
