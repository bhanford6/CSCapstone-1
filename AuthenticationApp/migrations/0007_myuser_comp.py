# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-06 07:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AuthenticationApp', '0006_auto_20161206_0530'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='comp',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
