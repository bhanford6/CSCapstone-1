# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-26 00:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectsApp', '0003_auto_20161121_2050'),
        ('AuthenticationApp', '0002_myuser_uname'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='bookmarks',
            field=models.ManyToManyField(to='ProjectsApp.Project'),
        ),
    ]
