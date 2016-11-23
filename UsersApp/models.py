from __future__ import unicode_literals

from django.db import models

# Create your models here.
class studentManager():
    def update_page(self, university=None, email=None, phone=None, about=None, skills=None):
        page = self.model(university=university, email=email, phone=phone, about=about, skills=skills)
        page.save(self._db)

class Student(models.Model):
    ident = models.AutoField(primary_key=True, default=0)
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
    objects = studentManager()

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
    #objects = professorManager()

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
    #objects = professorManager()
