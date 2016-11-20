from django.shortcuts import render

from . import models
from . import forms
from AuthenticationApp.models import MyUser
# Create your views here.
def getProfessors(request):
    professors_list = MyUser.objects.all()
    context = {
        'professors' : professors_list
    }
    return render(request, 'professors.html', context)
def getProfessorForm(request):
    return render(request, 'professorform.html')
def getProfessor(request):
    return render(request, 'professor.html')
