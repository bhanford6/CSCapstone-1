from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Student(models.Model):
    university = models.CharField(
        default=" ", 
        max_length=50, 
        null=True
    )
    email = models.EmailField(
        verbose_name='email address', 
        max_length=255, 
        unique=True
    )
    phone = models.CharField(
        default=" ",
        max_length=16,
        null=True
    )
    about = models.CharField(
        default=" ",
        max_length=100000,
        null=True
    )
    skills = models.CharField(
        default=" ",
        max_length=10000,
        null=True
    )
    def __str__(self):
        return self.name

class Professor(models.Model):
    university = models.CharField(
        default=" ", 
        max_length=50, 
        null=True
    )
    email = models.EmailField(
        verbose_name='email address', 
        max_length=255, 
        unique=True
    )
    phone = models.CharField(
        default=" ",
        max_length=16,
        null=True
    )
    about = models.CharField(
        default=" ",
        max_length=100000,
        null=True
    )
    projects = models.CharField(
        default=" ",
        max_length=10000,
        null=True
    )

class Engineer(models.Model):
    university = models.CharField(
        default=" ", 
        max_length=50, 
        null=True
    )
    email = models.EmailField(
        verbose_name='email address', 
        max_length=255, 
        unique=True
    )
    phone = models.CharField(
        default=" ",
        max_length=16,
        null=True
    )
    about = models.CharField(
        default=" ",
        max_length=100000,
        null=True
    )
    aboutcomp = models.CharField(
        default=" ",
        max_length=100000,
        null=True
    )
    projects = models.CharField(
        default=" ",
        max_length=10000,
        null=True
    )
