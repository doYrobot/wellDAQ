# encoding:utf-8
# 实现对登录表单字段是否符合规矩进行验证
from django import forms

# 登录页表单


class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput())

# 注册页表单


class SignupForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput())
    re_password = forms.CharField(widget=forms.PasswordInput())
    true_name = forms.CharField(max_length=30)
    department = forms.CharField(max_length=30)
    position = forms.CharField(max_length=30)
