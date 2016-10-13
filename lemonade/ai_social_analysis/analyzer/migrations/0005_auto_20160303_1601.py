# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-03 19:01
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('analyzer', '0004_auto_20160302_1734'),
    ]

    operations = [
        migrations.CreateModel(
            name='Algorithm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('function_name', models.CharField(max_length=40)),
            ],
        ),
        migrations.RenameField(
            model_name='task',
            old_name='function_parameters',
            new_name='algorithm_params',
        ),
        migrations.RemoveField(
            model_name='task',
            name='function',
        ),
        migrations.AddField(
            model_name='task',
            name='error',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='name',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='task',
            name='state',
            field=models.IntegerField(choices=[(1, 'Created'), (2, 'Running'), (3, 'Finished'), (4, 'Failed')], default=1),
        ),
        migrations.AddField(
            model_name='task',
            name='algorithm',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='analyzer.Algorithm'),
        ),
    ]