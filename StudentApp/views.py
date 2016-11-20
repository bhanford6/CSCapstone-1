from django.shortcuts import render

from . import models
from .import forms
from AuthenticationApp.models import MyUser
from AuthenticationApp.forms import UpdateForm
# Create your views here.
def getStudents(request):
    students_list = MyUser.objects.all()
    context = {
        'students' : students_list
    }
    return render(request, 'students.html', context)

def getStudentForm(request):
    form = UpdateForm(request.POST or None, instance=request.user)
    if form.is_valid():
        form.save()
        messages.success(request, 'Success, your page has been saved!')
    context = {
        "form" : form,
        "page_name" : "Bio"
    }
    return render(request, 'studentform.html', context)

def getStudent(request):
    return render(request, 'student.html')
