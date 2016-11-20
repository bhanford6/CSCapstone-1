"""ProjectsApp Views

Created by Harris Christiansen on 10/02/16.
"""
from django.shortcuts import render
from . import models
from . import forms
def getProjects(request):
	projects_list = models.Project.objects.all()
	return render(request, 'projects.html', {
        'projects': projects_list,
    })

def getProject(request):
    if request.user.is_authenticated():
        in_name = request.GET.get('name', 'None')
        in_project = models.Project.objects.get(name__exact=in_name)
        context = {
            'project' : in_project,
        }
        return render(request, 'project.html', context)
    # render error page if user is not logged in
    return render(request, 'autherror.html')

def getAddProject(request):
    return render(request, 'getaddproject.html')

def addProject(request):
    if request.method == 'POST':
        form = forms.ProjectForm(request.POST)
        if form.is_valid():
            new_project = models.Project(name=form.cleaned_data['name'], start=form.cleaned_data['start'], end=form.cleaned_data['end'], description=form.cleaned_data['description'], knowledge=form.cleaned_data['knowledge'], experience=form.cleaned_data['experience'])
            new_project.save()
            projects_list = models.Project.objects.all()
            context = {
               'projects' : projects_list,
            }
            return render(request, 'projects.html', context)
        else:
            form = forms.ProjectForm()
    return render(request, 'projects.html')
