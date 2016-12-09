"""
CompaniesApp Forms

Created by Jacob Dunbar on 10/3/2016.
"""
from django import forms
from ProjectsApp.models import Project

class CompanyForm(forms.Form):
    name = forms.CharField(label='Name', max_length=30)
    photo = forms.ImageField(label='Photo');
    description = forms.CharField(label='Description', max_length=300)
    website = forms.CharField(label='Website', max_length = 300)
    #company = Project.objects.get(name__exact="Base Project")
