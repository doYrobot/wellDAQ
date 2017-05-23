# encoding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
import json
from django.http import JsonResponse
# from django.core.urlresolvers import reverse

# Create your views here.


def index(request):
    return HttpResponse(u"返回纯文字")


# 返回html模板
def home(request):
    return render(request, 'comm_base.html')


# 返回html模板中带参数
def home2(request):
    # string = '通过参数传递来的字符串'
    list1 = ['jquery', 'bootstrap', 'javascript']
    return render(request, 'home.html', {'list': list1})


# 通过网址传参，利用request对象的GET方法获取
# 格式：/?a=3&b=4
def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a) + int(b)
    return render(request, 'home.html', {'c': c})


# 通过网址传参，利用request对象的GET方法获取
# 格式：/33/44
def add2(request, a, b):
    c = int(a) + int(b)
    return render(request, 'home.html', {'c': c})


def index2(request):
    return render(request, 'forms.html')


def login(request):
    return render(request, 'login.html')


def ajax(request):
    # a = request.GET.get('a')
    # b = request.GET.get('b')
    # c = int(a) + int(b)
    # c = 23
    return render(request, 'ajax.html')


def ajax_dict(request):
    mydict = {'subl': 'sublimetext', 'vim': 'linux vim'}
    return JsonResponse(mydict)


def ajax_add(request):
    a = request.GET.get('a')
    b = request.GET.get('b')
    c = int(a) + int(b)
    print c
    return HttpResponse(u"222")
