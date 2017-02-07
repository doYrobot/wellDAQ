# encoding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
import json
from django.http import JsonResponse
from accounts.forms import LoginForm
# from django.core.urlresolvers import reverse


# Create your views here.

def login(request):
    username = ''
    if request.method == "POST":  # 当提交表单时
        loginForm = LoginForm(request.POST)  # loginForm包含提交的数据 数据绑定
        if loginForm.is_valid():  # 如果提交的数据合法 数据验证
            username = loginForm.cleaned_data['username']
            # 取回传递来的数据 cleaned_data是一个字典
            # 跳转到主页
            return render(request, 'index_base.html', {'username': username})
    else:  # 当正常进入登录页面时
        loginForm = LoginForm()
        return render(request, 'login.html')


def signup(request):
    return render(request, 'signup.html')


def index(request):
    return render(request, 'index_base.html')


def loginout(request):
    return render(request, 'login.html')
