# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-05-03 21:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='create_datetime',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
