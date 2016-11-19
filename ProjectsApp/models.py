"""ProjectsApp Models

Created by Harris Christiansen on 10/02/16.
"""
from django.db import models
import datetime

class Project(models.Model):
    name = models.CharField(default=" ", max_length=200, null=True)

    start = models.DateField(default=datetime.date.today, null=True)
    end = models.DateField(default=datetime.date.today, null=True)
    description = models.CharField(default=" ", max_length=10000, null=True)
    knowledge = models.CharField(default=" ", max_length=10000, null=True)
    experience = models.CharField(default=" ", max_length=10000, null=True)
    #created_at = models.DateTimeField('date created')
    #updated_at = models.DateTimeField('date updated')

    def __str__(self):
        return self.name


