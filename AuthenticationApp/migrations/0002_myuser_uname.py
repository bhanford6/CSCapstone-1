# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-21 02:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AuthenticationApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='uname',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True),
        ),
    ]