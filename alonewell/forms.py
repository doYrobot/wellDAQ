# encoding:utf-8
# 实现对表单字段是否符合规矩进行验证

from django import forms
from models import WellBasicData

# 添加单井数据表单


class AddWellForm(forms.Form):
    wellNo = forms.IntegerField()
    wellName = forms.CharField(max_length=30)
    dimension = forms.FloatField()  # 维度
    longitude = forms.FloatField()  # 经度


class AddOperateParametersForm(forms.Form):
    wellNo = forms.IntegerField()
    data_storage = forms.DateField()
    targetpress = forms.FloatField()
    presentpress = forms.FloatField()
    bottompress = forms.FloatField()
    targetflow = forms.IntegerField()
    presentflow = forms.IntegerField()
    totalflow = forms.IntegerField()
    dailyflow = forms.IntegerField()
    cycle = forms.IntegerField()
    stepRange = forms.FloatField()
    instantLP = forms.FloatField()
    totalLP = forms.FloatField()
    valvelift = forms.IntegerField()

    def clean_wellNo(self):
        wellNo = self.cleaned_data['wellNo']
        if wellNo:
            if WellBasicData.objects.get(wellNo=wellNo):
                return WellBasicData.objects.get(wellNo=wellNo)
            else:
                raise forms.ValidationError(u'无此井号请查询后再次输入')

        else:
            raise forms.ValidationError(u'井号不能为空')
