# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-05-12 06:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('alonewell', '0006_operateparameters'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operateparameters',
            name='wellNo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='No', to='alonewell.WellBasicData'),
        ),
    ]
