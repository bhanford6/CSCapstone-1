"""ProjectsApp URL Configuration

Created by Harris Christiansen on 10/02/16.
"""
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^project/all$', views.getProjects, name='Projects'),
    url(r'^project$', views.getProject, name='Project'),
    url(r'^getaddproject$', views.getAddProject, name='GetAddProject'),
    url(r'^addproject$', views.addProject, name='AddProject'),
    
]
