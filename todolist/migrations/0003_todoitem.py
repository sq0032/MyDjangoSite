# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-05-04 04:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0002_auto_20160503_1705'),
    ]

    operations = [
        migrations.CreateModel(
            name='TodoItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('create_datetime', models.DateTimeField(auto_now_add=True)),
                ('todolist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todolist.TodoList')),
            ],
        ),
    ]