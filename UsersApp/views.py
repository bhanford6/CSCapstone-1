from django.shortcuts import render
import sys
import re
from . import models
from . import forms
from .models import Student
from AuthenticationApp.models import MyUser
# Create your views here.

# Display table of all professors
def getProfessors(request):
    professors_list = MyUser.objects.get(is_professor=True)
    context = {
        'professors' : professors_list
    }
    return render(request, 'professors.html', context)

# Display table of all students
def getStudents(request):
    students_list = MyUser.objects.get(is_student=True)
    context = {
        'students' : students_list
    }
    return render(request, 'students.html', context)

# Display table of all engineers
def getEngineers(request):
    engineers_list = MyUser.objects.get(is_engineer=True)
    context= {
        'engineers' : engineers_list
    }
    return render(request, 'engineers.html', context)

# Display table of all users
def getUsers(request):
    users_list = MyUser.objects.all()
    context = {
        'users' : users_list
    }
    return render(request, 'users.html', context)

# Form to edit user's profile page
def getUserForm(request):
    email = request.user.email
    r = re.compile("(@?[^@]+)")
    tup = r.findall(email)
    unique_name = tup[0]
    # I want to grab the fields from the model of the form
    # that have already been filled out. I have to grab
    # from the model based on student/prof/engineer
    # Need to make sure and update the model
    if request.method == 'POST':
        print "method is POST"
        form = forms.UserForm(request.POST or None)
        if form.is_valid():
            print "valid"
            student = models.Student(
                #first_name=form.cleaned_data['first_name'],
                #last_name=form.cleaned_data['last_name'],
                university=form.cleaned_data['university'],
                email=form.cleaned_data['email'],
                phone=form.cleaned_data['phone'],
                about=form.cleaned_data['about'],
                skills=form.cleaned_data['skills'],
            )
            student.save()
            student_attr = models.Student.objects.all()
            print len(student_attr)

            context = {
                'student_attr'  : student_attr,
                'uname'         : unique_name,
                'is_student'    : request.user.is_student,
                'is_professor'  : request.user.is_professor,
                'is_engineer'   : request.user.is_engineer,
            }
            return render(request, 'userform.html', context)
        else:
            form = forms.UserForm()
            form.save()
            
    print "whats going on?"
    context = {
        'uname'         : unique_name,
        'is_student'    : request.user.is_student,
        'is_professor'  : request.user.is_professor,
        'is_engineer'   : request.user.is_engineer,
    }
    return render(request, 'userform.html', context)

# Display of users's profile page
def getUser(request):
    if request.user.is_authenticated():
        email = request.user.email
        r = re.compile("(@?[^@]+)")
        tup = r.findall(email)
        unique_name = tup[0]
        uname = request.GET.get('name','None')
        user = MyUser.objects.get(uname__exact=uname)
        print user.email
        user_page = models.Student.objects.get(email__exact=user.email)
        print user_page
        context = {
            'user'          : user,
            'uname'         : unique_name,
            'is_student'    : request.user.is_student,
            'is_professor'  : request.user.is_professor,
            'is_engineer'   : request.user.is_engineer,
        }
        return render(request, 'user.html', context)
    return render(request, 'autherror.html')

# Display other users's profile page
def getOtherUser(request):
    in_name = request.GET.get('name', 'None')
    print request.user.uname
    print "nothing"
    print in_name
    other_user =  MyUser.objects.get(uname__exact=in_name)
    print other_user
    r = re.compile("(@?[^@]+)")
    tup = r.findall(other_user.email)
    unique_name = tup[0]
    print unique_name
    print other_user.is_engineer
    context = {
        'uname'         : unique_name,
        'first_name'    : other_user.first_name,
        'last_name'     : other_user.last_name,
        'is_student'    : other_user.is_student,
        'is_professor'  : other_user.is_professor,
        'is_engineer'   : other_user.is_engineer,
    }
    return render(request, 'otheruser.html', context)







