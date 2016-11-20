from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^professor/all$', views.getProfessors, name='Professors'),
    url(r'^professor/form$', views.getProfessorForm, name='ProfessorForm'),
    url(r'^professor$', views.getProfessor, name='Proffesor'),
]
