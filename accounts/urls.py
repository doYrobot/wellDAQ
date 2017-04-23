# encoding:utf-8

from django.conf.urls import url
from accounts import views
# from django.contrib import admin


urlpatterns = [
    url(r'^$', views.mylogin, name='login'),
    url(r'signup$', views.signup, name='signup'),
    url(r'index$', views.index, name='index'),
    url(r'loginout$', views.loginout, name='loginout'),
]
