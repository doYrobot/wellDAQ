# encoding:utf-8
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import json
from django.http import JsonResponse
from accounts.forms import LoginForm, SignupForm
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.urls import reverse
from models import UserProfile, Department, Position
# from django.core.urlresolvers import reverse


# 登录主界面

def mylogin(request):
    username = ''
    password = ''
    if request.user.is_authenticated():  # 判断是否已经有登录的用户
        return HttpResponseRedirect('/index')
    if request.method == "POST":  # 当提交表单时
        loginForm = LoginForm(request.POST)  # loginForm包含提交的数据 数据绑定
        if loginForm.is_valid():  # 如果提交的数据合法 数据验证
            username = loginForm.cleaned_data['username']
            password = loginForm.cleaned_data['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                login(request, user)  # 将user存入session
                request.session['username'] = username
                return HttpResponseRedirect('/index')
            else:
                loginForm = LoginForm()
                return render(request, 'login.html')
            # 取回传递来的数据 cleaned_data是一个字典
            # 跳转到主页
            # return render(request, 'index_base.html', {'username': username})
    else:  # 当正常进入登录页面时
        loginForm = LoginForm()
        return render(request, 'login.html')


def signup(request):
    username = ''
    password = ''
    re_password = ''
    true_name = ''
    department = ''
    position = ''
    errors = ''
    if request.method == 'POST':
        signupForm = SignupForm(request.POST)
        if signupForm.is_valid():
            username = signupForm.cleaned_data['username']
            password = signupForm.cleaned_data['password']
            re_password = signupForm.cleaned_data['re_password']
            true_name = signupForm.cleaned_data['true_name']  # 姓名
            department = signupForm.cleaned_data['department']  # 部门
            position = signupForm.cleaned_data['position']  # 职位
            if password != re_password:
                errors = '两次输入的密码不一致'
                return render(request, 'signup.html', {'errors': errors})
            filterResult = User.objects.filter(username=username)
            if len(filterResult) > 0:
                errors = '该用户已经存在'
                return render(request, 'signup.html', {'errors': errors})
            user = User()
            user.username = username
            user.set_password(password)

            user.save()

            userProfile = UserProfile()
            userProfile.user_id = user.id
            userProfile.true_name = true_name
            userProfile.department = department
            userProfile.position = position
            userProfile.save()

            newUser = auth.authenticate(username=username, password=password)
            if newUser is not None:
                login(request, newUser)
                return render(request, 'index_base.html', {'username': username})
                # return HttpResponse('注册成功') 测试代码
        else:
            return render(request, 'signup.html', {'form': signupForm})
    # 如果不是提交数据，返回空白的注册表单
    else:
        signupForm = SignupForm()

        return render(request, 'signup.html')


@login_required
def index(request):
    username = request.session.get('username')
    user = User.objects.get(username=username)
    return render(request, 'index_base.html', {'username': username, 'user': user})


@login_required
def loginout(request):
    logout(request)  # 清除session中的user
    return HttpResponseRedirect('/')

# 补全用户详细信息，如设置头像等


@login_required
def set_user_detail(request, template_name='set_user_detail.html'):
    return render(request, template_name)  # 需要编写详细信息模板

# 设置用户权限


@login_required
def set_user_permissions(request, template_name='set_userpermissions.html'):

    return render(request, template_name)
# 创建部门数据


@login_required
def create_department(request, template_name='query_department.html'):

    # department=Department.objects.get_or_create()
    return render(request, template_name)
# 创建职位数据


@login_required
def create_position(request, template_name='query_position.html'):
    return render(request, template_name)

# 创建权限数据


@login_required
def create_permissions(request, template_name='set_userpermissions.html'):
    return render(request, template_name)
