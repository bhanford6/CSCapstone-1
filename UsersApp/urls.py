from django.conf.urls import url

from .import views

urlpatterns = [
    url(r'^user$', views.getUser, name='User'),
    url(r'^users/all$', views.getUsers, name='Users'),
    url(r'^user/other$', views.getOtherUser, name='OtherUser'),
    url(r'^user/form$', views.getUserForm, name='UserForm'),

    url(r'^student/all$', views.getStudents, name='Students'),
    url(r'^student/form$', views.getUserForm, name='StudentForm'),
    url(r'^student$', views.getUser, name='Student'),

    url(r'^professor/all$', views.getProfessors, name='Professors'),
    url(r'^professor/form$', views.getUserForm, name='ProfessorForm'),
    url(r'^professor$', views.getUser, name='Proffesor'),

    url(r'^engineer/all$', views.getEngineers, name='Engineers'),
    url(r'^engineer/form$', views.getUserForm, name='EngineerForm'),
    url(r'^engineer$', views.getUser, name='Engineer'),
]

