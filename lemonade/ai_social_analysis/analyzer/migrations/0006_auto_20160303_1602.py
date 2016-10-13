# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-03 19:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('analyzer', '0005_auto_20160303_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='algorithm',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='analyzer.Algorithm'),
        ),
        migrations.AlterField(
            model_name='task',
            name='name',
            field=models.CharField(max_length=60),
        ),
    ]
