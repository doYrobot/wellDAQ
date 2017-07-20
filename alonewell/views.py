# encoding:utf-8

from django.shortcuts import render
from forms import AddWellForm, AddOperateParametersForm
from models import WellBasicData, OperateParameters
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.contrib.auth.decorators import login_required
import json

# Create your views here.

# 添加或者更新基础井位信息

import sys
reload(sys)
sys.setdefaultencoding('utf8')


@login_required
def addwell(request):
    if request.method == 'POST':
        addWellForm = AddWellForm(request.POST)
        if addWellForm.is_valid():
            wellNo = addWellForm.cleaned_data['wellNo']
            wellName = addWellForm.cleaned_data['wellName']
            dimension = addWellForm.cleaned_data['dimension']
            longitude = addWellForm.cleaned_data['longitude']
            # 其返回值为元组，（对象，ture或者false）
            if WellBasicData.objects.filter(wellNo=wellNo):
                wellobject = WellBasicData.objects.get(wellNo=wellNo)
            else:
                wellobject = WellBasicData()
            wellobject.wellNo = wellNo
            wellobject.wellName = wellName
            wellobject.dimension = dimension
            wellobject.longitude = longitude
            wellobject.save()
            return HttpResponseRedirect('alonewell/query_well')
    else:
        addWellForm = AddWellForm()
        return render(request, 'addwell.html')

# 查询所有井位信息


@login_required
def query_well(request):
    # 通过查询得到满足条件的所有对象列表，最后将对象列表返回到模板
    # 在模板中采用for循环读出对象，逐个显示
    items = WellBasicData.objects.all()
    return render(request, 'query_well.html', {'items': items})  # 查询所有井位信息

# 删除某行井位信息


@login_required
def query_well_del(request, wellno):
    # 通过查询得到满足条件的所有对象列表，最后将对象列表返回到模板
    # 在模板中采用for循环读出对象，逐个显示
    WellBasicData.objects.filter(wellNo=wellno).delete()
    items = WellBasicData.objects.all()
    return render(request, 'query_well.html', {'items': items})

# 添加单井运行参数


@login_required
def add_operate_parameters(request, templatename='add_operateparameters.html'):
    if request.method == 'POST':
        addOperateParametersForm = AddOperateParametersForm(request.POST)
        if addOperateParametersForm.is_valid():
            wellNo = addOperateParametersForm.cleaned_data['wellNo']
            data_storage = addOperateParametersForm.cleaned_data[
                'data_storage']
            targetpress = addOperateParametersForm.cleaned_data['targetpress']
            presentpress = addOperateParametersForm.cleaned_data[
                'presentpress']
            bottompress = addOperateParametersForm.cleaned_data['bottompress']
            targetflow = addOperateParametersForm.cleaned_data['targetflow']
            presentflow = addOperateParametersForm.cleaned_data['presentflow']
            totalflow = addOperateParametersForm.cleaned_data['totalflow']
            dailyflow = addOperateParametersForm.cleaned_data['dailyflow']
            cycle = addOperateParametersForm.cleaned_data['cycle']
            stepRange = addOperateParametersForm.cleaned_data['stepRange']
            instantLP = addOperateParametersForm.cleaned_data['instantLP']
            totalLP = addOperateParametersForm.cleaned_data['totalLP']
            valvelift = addOperateParametersForm.cleaned_data['valvelift']
            operateParametersObject = OperateParameters()
            operateParametersObject.wellNo = wellNo
            operateParametersObject.data_storage = data_storage
            operateParametersObject.targetpress = targetpress
            operateParametersObject.presentpress = presentpress
            operateParametersObject.bottompress = bottompress
            operateParametersObject.targetflow = targetflow
            operateParametersObject.presentflow = presentflow
            operateParametersObject.totalflow = totalflow
            operateParametersObject.dailyflow = dailyflow
            operateParametersObject.cycle = cycle
            operateParametersObject.stepRange = stepRange
            operateParametersObject.instantLP = instantLP
            operateParametersObject.totalLP = totalLP
            operateParametersObject.valvelift = valvelift
            operateParametersObject.save()
            return HttpResponseRedirect('alonewell/query_parameters')
        else:
            return render(request, 'add_operateparameters.html', {'form': addOperateParametersForm})

    else:
        return render(request, 'add_operateparameters.html')
# 将采集数据全部返回


@login_required
def query_parameters(request):
    items = OperateParameters.objects.all()
    return render(request, 'query_parameters.html', {'items': items})

# 删除一行参数


@login_required
def query_parameters_del(request, parameters_id):
    OperateParameters.objects.filter(id=parameters_id).delete()
    return HttpResponseRedirect('alonewell/query_parameters')
# 通过AJAX查询井号是否已经保存


@login_required
def isvalid_wellNo(request):
    if request.method == 'GET':
        wellNo = request.GET['wellNo']
        print wellNo
        obj_well = WellBasicData.objects.get(wellNo=wellNo)
        obj_well_json = {'wellName': obj_well.wellName,
                         'dimension': obj_well.dimension, 'longitude': obj_well.longitude}
        if obj_well:
            wellNo_result = {'result': obj_well_json, 'wellNo': wellNo}
        else:
            wellNo_result = {'result': 'wrong', 'wellNo': wellNo}

    return JsonResponse(wellNo_result)


@login_required
def test(request):
    username = request.session.get('username')
    print username
    return render(request, 'test.html', {'username': username})
    # return render(request, 'test.html')


@login_required
def test01(request):
    if request.method == 'GET':
        if request.GET['wellNo']:
            wellNo = request.GET['wellNo']
            if WellBasicData.objects.get(wellNo=wellNo):
                # object_wellNo = WellBasicData.objects.filter(wellNo=wellNo)
                result = serializers.serialize(
                    'json', WellBasicData.objects.filter(wellNo=wellNo))
                # result = WellBasicData.objects.filter(wellNo=wellNo)
                print type(result)
                return HttpResponse(result, content_type="application/json")
        else:
            return render(request, 'test.html')
    else:
        return render(request, 'test.html')
