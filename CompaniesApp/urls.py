"""CompaniesApp URL Configuration

Created by Jacob Dunbar on 10/2/2016.
"""
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^company/all$', views.getCompanies, name='Companies'),
    url(r'^company/form$', views.getCompanyForm, name='CompanyForm'),
    url(r'^company/formsuccess$', views.getCompanyFormSuccess, name='CompanyFormSuccess'),
    url(r'^company/join$', views.joinCompany, name='JoinCompany'),
    url(r'^company/unjoin$', views.unjoinCompany, name='UnjoinCompany'),
    url(r'^company$', views.getCompany, name='Company'),
    url(r'^company/projects$', views.getCompProjects, name='CompProjects'),
    url(r'^company/project/add$', views.addProject, name='AddProject'),
    url(r'^company/project/added$', views.projectAdded, name='ProjectAdded'),
    url(r'^company/other/project$', views.otherCompProj, name='OtherCompProj'),
    #url(r'^company/project/add/success$', views.projAddSuccess, name='ProjAddSuccess'),
    url(r'^company/project/form$', views.compProjForm, name='CompProjForm'),
]
