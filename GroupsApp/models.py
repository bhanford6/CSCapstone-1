"""GroupsApp Models

Created by Naman Patwari on 10/10/2016.
"""
from django.db import models
from AuthenticationApp.models import MyUser
from ProjectsApp.models import Project
from CommentsApp.models import Comment

# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=300)
    members = models.ManyToManyField(MyUser)
#    project = models.ManyToManyField(Project)
    project = models.OneToOneField(Project, on_delete=models.CASCADE, primary_key=False, default="", blank=True, null=True)
    comments = models.ManyToManyField(Comment) 
    def __str__(self):
        return self.name
