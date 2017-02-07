# encoding:utf-8
# 实现对登录表单字段是否符合规矩进行验证
from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput())
