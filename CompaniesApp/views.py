"""
CompaniesApp Views

Created by Jacob Dunbar on 10/2/2016.
"""
from django.shortcuts import render

from . import models
from . import forms
from ProjectsApp.models import Project
from GroupsApp.models import Group

def getCompanies(request):
    if request.user.is_authenticated():
        companies_list = models.Company.objects.all()
        context = {
            'companies' : companies_list,
        }
        return render(request, 'companies.html', context)
    # render error page if user is not logged in
    return render(request, 'autherror.html')

def getCompany(request):
    print "why am I here?"
    if request.user.is_authenticated():
        in_name = request.GET.get('name', 'None')
        in_company = models.Company.objects.get(name__exact=in_name)
        is_member = in_company.members.filter(email__exact=request.user.email)
        user = request.user
        context = {
            'company' : in_company,
            'userIsMember': is_member,
            'user' : user,
        }
        return render(request, 'company.html', context)
    # render error page if user is not logged in
    return render(request, 'autherror.html')

def getCompanyForm(request):
    if request.user.is_authenticated():
        return render(request, 'companyform.html')
    # render error page if user is not logged in
    return render(request, 'autherror.html')

def getCompanyFormSuccess(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            form = forms.CompanyForm(request.POST, request.FILES)
            if form.is_valid():
                if models.Company.objects.filter(name__exact=form.cleaned_data['name']).exists():
                    return render(request, 'companyform.html', {'error' : 'Error: That company name already exists!'})
                new_company = models.Company(name=form.cleaned_data['name'], 
                                             photo=request.FILES['photo'],  
                                             description=form.cleaned_data['description'],
                                             website=form.cleaned_data['website'])
                new_company.save()
                context = {
                    'name' : form.cleaned_data['name'],
                }
                return render(request, 'companyformsuccess.html', context)
            else:
                return render(request, 'companyform.html', {'error' : 'Error: Photo upload failed!'})
        else:
            form = forms.CompanyForm()
        return render(request, 'companyform.html')
    # render error page if user is not logged in
    return render(request, 'autherror.html')

def joinCompany(request):
    if request.user.is_authenticated():
        in_name = request.GET.get('name', 'None')
        in_company = models.Company.objects.get(name__exact=in_name)
        in_company.members.add(request.user)
        in_company.save();
        request.user.company_set.add(in_company)
        request.user.save()
        context = {
            'company' : in_company,
            'userIsMember': True,
        }
        return render(request, 'company.html', context)
    return render(request, 'autherror.html')
    
def unjoinCompany(request):
    if request.user.is_authenticated():
        in_name = request.GET.get('name', 'None')
        in_company = models.Company.objects.get(name__exact=in_name)
        in_company.members.remove(request.user)
        in_company.save();
        request.user.company_set.remove(in_company)
        request.user.save()
        context = {
            'company' : in_company,
            'userIsMember': False,
        }
        return render(request, 'company.html', context)
    return render(request, 'autherror.html')
   
def getCompProjects(request):
    print "entered"
    if request.user.is_authenticated():
        print "into"
        in_name = request.GET.get('name', 'None')
        in_company = models.Company.objects.get(name__exact=in_name)
        project_list = in_company.projects.all()
        is_member = in_company.members.filter(email__exact=request.user.email)
        user = request.user
        
        context = {
            'company'       : in_company,
            'projects'      : project_list,
            'userIsMember'  : is_member,
            'user'          : user,
        }
        return render(request, 'companyprojects.html', context)
    return render(request, 'autherror.html')

def addProject(request):
    print "entered"
    if request.user.is_authenticated():
        in_name = request.GET.get('name', 'None')
        in_company = models.Company.objects.get(name__exact=in_name)
        project_list = Project.objects.all()
        is_member = in_company.members.filter(email__exact=request.user.email)
        user = request.user
        context = {
            'company'       : in_company,
            'projects'      : project_list,
            'userIsMember'  : is_member,
            'user'          : user,
        }
        return render(request, 'addproject.html', context)
    return render(request, 'autherror.html')

def projectAdded(request):
    if request.user.is_authenticated():
        in_name = request.GET.get('name', 'None')
        in_project = request.GET.get('project', 'None')
        in_company = models.Company.objects.get(name__exact=in_name)
        project_list = in_company.projects.all()
        project = models.Project.objects.get(name__exact=in_project)
        in_company.projects.add(project)
        in_company.save()
        is_member = in_company.members.filter(email__exact=request.user.email)
        user = request.user
        context = {
          'company'         : in_company,
          'projects'        : project_list,
          'project'         : project,
          'userIsMember'    : is_member,
          'user'            : user,
        }
        return render(request, 'projectadded.html', context)
    return render(request, 'autherror.html')
   
def otherCompProj(request):
    if request.user.is_authenticated():
        in_name = request.GET.get('name', 'None')
        in_company = models.Company.objects.get(name__exact=in_name)
        in_project = request.GET.get('project', 'None')
        project = models.Project.objects.get(name__exact=in_project)
        user = request.user
        context = {
            'company'   : in_company,
            'project'   : project,
            'user'      : user,
        }
        return render(request, 'othercompproj.html', context)
    return render(request, 'autherror.html')

def cloneCompProj(request):
    if request.user.is_authenticated():
        in_name = request.GET.get('name', 'None')
        in_company = models.Company.objects.get(name__exact=in_name)
        in_project = request.GET.get('project', 'None')
        project = models.Project.objects.get(name__exact=in_project)
        user = request.user
        in_company.projects.add(project)
        in_company.save()
        context = {
            'project'   : project,
            'company'   : in_company,
            'user'      : user,
        }
        return render(request, 'projectadded.html', context)
    return render(request, 'autherror.html')

def compProjForm(request):
    if request.user.is_authenticated():
        in_company = request.GET.get('name', 'None')
        company = models.Company.objects.get(name__exact=in_company)
        if request.method == 'POST':
            form = forms.ProjectForm(request.POST)
            if form.is_valid():
                new_project = Project(name=form.cleaned_data['name'], start=form.cleaned_data['start'], end=form.cleaned_data['end'], description=form.cleaned_data['description'], knowleedge=form.cleaned_data['knowledge'], experience=form.cleaned_data['experience'])
                new_project.save()
                print len(company.projects)
                company.projects.add(new_project)
                company.projects.save()
                print len(company.projects)
                print "hello?"
                projects_list = models.Project.objects.all()
                context = {
                    'projects' : projects_list,
                }
                return render(request, 'compprojform.html', context)
            else:
                form = forms.ProjectForm()
        return render(request, 'compprojform.html')
    return render(request, 'autherror.html')
