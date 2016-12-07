# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-06 04:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectsApp', '0003_auto_20161121_2050'),
        ('AuthenticationApp', '0003_myuser_bookmarks'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='bookmarks',
        ),
        migrations.AddField(
            model_name='myuser',
            name='bookmarks',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ProjectsApp.Project'),
        ),
    ]
