# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-05-01 14:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('alonewell', '0005_auto_20170501_2121'),
    ]

    operations = [
        migrations.CreateModel(
            name='OperateParameters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_storage', models.DateField()),
                ('targetpress', models.FloatField()),
                ('presentpress', models.FloatField()),
                ('bottompress', models.FloatField()),
                ('targetflow', models.IntegerField()),
                ('presentflow', models.IntegerField()),
                ('totalflow', models.IntegerField()),
                ('dailyflow', models.IntegerField()),
                ('cycle', models.IntegerField()),
                ('stepRange', models.FloatField()),
                ('instantLP', models.FloatField()),
                ('totalLP', models.FloatField()),
                ('valvelift', models.IntegerField()),
                ('wellNo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alonewell.WellBasicData')),
            ],
        ),
    ]
