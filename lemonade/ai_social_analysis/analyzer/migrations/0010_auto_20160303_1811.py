# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-03 21:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('analyzer', '0009_auto_20160303_1808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='dataset_input',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='task_children', to='analyzer.Dataset'),
        ),
        migrations.AlterField(
            model_name='task',
            name='dataset_output',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='task_parent', to='analyzer.Dataset'),
        ),
    ]
