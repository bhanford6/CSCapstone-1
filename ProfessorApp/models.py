from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Professor(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
