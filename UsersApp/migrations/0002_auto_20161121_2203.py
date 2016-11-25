# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-21 22:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UsersApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='EngineerForm',
            new_name='Engineer',
        ),
        migrations.RenameModel(
            old_name='StudentForm',
            new_name='Professor',
        ),
        migrations.RenameModel(
            old_name='ProfessorForm',
            new_name='Student',
        ),
        migrations.RenameField(
            model_name='professor',
            old_name='skills',
            new_name='projects',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='projects',
            new_name='skills',
        ),
    ]