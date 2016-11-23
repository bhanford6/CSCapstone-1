from django.shortcuts import render
import sys
import re
from . import models
from . import forms
from .models import Student
from AuthenticationApp.models import MyUser
# Create your views here.

class identity():
    i = 1

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
    try:
        if request.user.is_student:
            cur_stud = models.Student.objects.get(ident__exact=request.user.id)
        elif request.user.is_professor:
            cur_prof = models.Professor.objects.get(ident__exact=request.user.id)
        elif request.user.is_engineer:
            cur_eng = models.Engineer.objects.get(ident__exact=request.user.id)
    except:
        cur_stud = None
        cur_prof = None
        cur_eng  = None
    # I want to grab the fields from the model of the form
    # that have already been filled out. I have to grab
    # from the model based on student/prof/engineer
    # Need to make sure and update the model
    if request.method == 'POST' and request.user.is_student:
        # create a field in the model that has an id 
        # so we can check if current id exists
        # then update instead of creating a new student object
        print "why you come here?"
        form = forms.StudentForm(request.POST)
        if form.is_valid() and cur_stud==None:
            student = models.Student(
                ident=request.user.id,
                university=form.cleaned_data['university'],
                email=form.cleaned_data['email'],
                phone=form.cleaned_data['phone'],
                about=form.cleaned_data['about'],
                skills=form.cleaned_data['skills'],
            )
            student.save()
            cur_stud = student
        elif form.is_valid():
            cur_stud.university=form.cleaned_data['university']
            cur_stud.email=form.cleaned_data['email']
            cur_stud.phone=form.cleaned_data['phone']
            cur_stud.about=form.cleaned_data['about']
            cur_stud.skills=form.cleaned_data['skills']
            cur_stud.save()
        student_attr = models.Student.objects.all()
        context = {
            'student_attr'  : student_attr,
            'uname'         : unique_name,
            'is_student'    : request.user.is_student,
            'is_professor'  : request.user.is_professor,
            'is_engineer'   : request.user.is_engineer,
        }
        return render(request, 'userform.html', context)
    elif request.method == 'POST' and request.user.is_professor:
        form = forms.ProfessorForm(request.POST)
        if form.is_valid() and cur_prof == None:
            professor = models.Professor(
                ident=request.user.id,
                university=form.cleaned_data['university'],
                email=form.cleaned_data['email'],
                phone=form.cleaned_data['phone'],
                about=form.cleaned_data['about'],
                classes=form.cleaned_data['classes'],
            )
            professor.save()
            cur_prof = professor
        elif form.is_valid():
            cur_prof.university=form.cleaned_data['university']
            cur_prof.email=form.cleaned_data['email']
            cur_prof.phone=form.cleaned_data['phone']
            cur_prof.about=form.cleaned_data['about']
            cur_prof.classes=form.cleaned_data['classes']
            cur_prof.save()
        professor_attr = models.Professor.objects.all()
        context = {
            'professor_attr'    : professor_attr,
            'uname'             : unique_name,
            'is_student'        : request.user.is_student,
            'is_professor'      : request.user.is_professor,
            'is_engineer'       : request.user.is_engineer,
        }
        return render(request, 'userform.html', context)
    elif request.method == 'POST' and request.user.is_engineer:
        form = forms.EngineerForm(request.POST)
        print form.errors
        if form.is_valid() and cur_eng == None:
            print "in"
            engineer = models.Engineer(
                ident=request.user.id,
                university=form.cleaned_data['university'],
                email=form.cleaned_data['email'],
                phone=form.cleaned_data['phone'],
                about=form.cleaned_data['about'],
                aboutcomp=form.cleaned_data['aboutcomp'],
                projects=form.cleaned_data['projects'],
            )
            engineer.save()
            cur_eng = engineer
        elif form.is_valid():
            cur_eng.university=form.cleaned_data['university']
            cur_eng.email=form.cleaned_data['email']
            cur_eng.phone=form.cleaned_data['phone']
            cur_eng.about=form.cleaned_data['about']
            cur_eng.aboutcomp=form.cleaned_data['aboutcomp']
            cur_eng.projects=form.clenaed_data['projects']
            cur_eng.save()
        engineer_attr = models.Engineer.objects.all()
        context = {
            'engineer_attr'     : engineer_attr,
            'uname'             : unique_name,
            'is_student'        : request.user.is_student,
            'is_professor'      : request.user.is_professor,
            'is_engineer'       : request.user.is_engineer,
        }
        return render(request, 'userform.html', context)
        
                
    elif request.method == 'GET':
        if request.user.is_student and cur_stud != None:
            form = forms.StudentForm(request.POST, initial={
                'university'    : cur_stud.university,
                'email'         : cur_stud.email,
                'phone'         : cur_stud.phone,
                'about'         : cur_stud.about,
                'skills'        : cur_stud.skills,
            })
        elif request.user.is_professor and cur_prof != None:
            form = forms.ProfessorForm(request.POST, initial={
                'university'    : cur_prof.university,
                'email'         : cur_prof.email,
                'phone'         : cur_prof.phone,
                'about'         : cur_prof.about,
                'classes'       : cur_prof.classes,
            })
        elif request.user.is_engineer and cur_eng !=None:
            form = forms.EngineerForm(request.POST, initial={
                'university'    : cur_eng.university,
                'email'         : cur_eng.email,
                'phone'         : cur_eng.phone,
                'about'         : cur_eng.about,
                'aboutcomp'     : cur_eng.aboutcomp,
                'projects'      : cur_eng.projects,
            })
    context = {
        #'form'          : form,
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
        if user.is_student:
            user_page = models.Student.objects.get(ident__exact=user.id)
        elif user.is_professor:
            user_page = models.Professor.objects.get(ident__exact=user.id)
        elif user.is_engineer:
            user_page = models.Engineer.objects.get(ident__exact=user.id)
        print user_page
        context = {
            'user_page'     : user_page,
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







