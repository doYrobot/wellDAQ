# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-07-09 17:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('alonewell', '0007_auto_20170512_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operateparameters',
            name='bottompress',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='operateparameters',
            name='cycle',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='operateparameters',
            name='dailyflow',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='operateparameters',
            name='data_storage',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='operateparameters',
            name='instantLP',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='operateparameters',
            name='presentflow',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='operateparameters',
            name='presentpress',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='operateparameters',
            name='stepRange',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='operateparameters',
            name='targetflow',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='operateparameters',
            name='targetpress',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='operateparameters',
            name='totalLP',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='operateparameters',
            name='totalflow',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='operateparameters',
            name='valvelift',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='operateparameters',
            name='wellNo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wellmodel', to='alonewell.WellBasicData'),
        ),
    ]
