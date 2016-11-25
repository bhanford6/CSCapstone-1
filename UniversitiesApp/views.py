"""
UniversitiesApp Views
Created by Jacob Dunbar on 11/5/2016.
"""
from django.shortcuts import render

from . import models
from . import forms
from AuthenticationApp.models import MyUser

def getUniversities(request):
    if request.user.is_authenticated():
        universities_list = models.University.objects.all()
        context = {
            'universities' : universities_list,
        }
        return render(request, 'universities.html', context)
    # render error page if user is not logged in
    return render(request, 'autherror.html')

def getUniversity(request):
    if request.user.is_authenticated():
        in_name = request.GET.get('name', 'None')
        in_university = models.University.objects.get(name__exact=in_name)
        is_member = in_university.members.filter(email__exact=request.user.email)
        universities_list = models.University.objects.all()
        joinable = True
        for university in universities_list:
            if university.members.filter(email__exact=request.user.email):
                joinable = False

        context = {
            'joinable'      : joinable,
            'university'    : in_university,
            'userIsMember'  : is_member,
        }
        return render(request, 'university.html', context)
    # render error page if user is not logged in
    return render(request, 'autherror.html')

def getUniversityForm(request):
    if request.user.is_authenticated():
        return render(request, 'universityform.html')
    # render error page if user is not logged in
    return render(request, 'autherror.html')

def getUniversityFormSuccess(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            form = forms.UniversityForm(request.POST, request.FILES)
            if form.is_valid():
                if models.University.objects.filter(name__exact=form.cleaned_data['name']).exists():
                    return render(request, 'universityform.html', {'error' : 'Error: That university name already exists!'})
                new_university = models.University(name=form.cleaned_data['name'], 
                                             photo=request.FILES['photo'],  
                                             description=form.cleaned_data['description'],
                                             website=form.cleaned_data['website'])
                new_university.save()
                context = {
                    'name' : form.cleaned_data['name'],
                }
                return render(request, 'universityformsuccess.html', context)
            else:
                return render(request, 'universityform.html', {'error' : 'Error: Photo upload failed!'})
        else:
            form = forms.UniversityForm()
        return render(request, 'universityform.html')
    # render error page if user is not logged in
    return render(request, 'autherror.html')

def joinUniversity(request):
    if request.user.is_authenticated():
        in_name = request.GET.get('name', 'None')
        in_university = models.University.objects.get(name__exact=in_name)
        in_university.members.add(request.user)
        in_university.save();
        request.user.university_set.add(in_university)
        request.user.save()
        context = {
            'university' : in_university,
            'userIsMember': True,
        }
        return render(request, 'university.html', context)
    return render(request, 'autherror.html')
    
def unjoinUniversity(request):
    if request.user.is_authenticated():
        in_name = request.GET.get('name', 'None')
        in_university = models.University.objects.get(name__exact=in_name)
        in_university.members.remove(request.user)
        in_university.save();
        request.user.university_set.remove(in_university)
        request.user.save()
        context = {
            'university' : in_university,
            'userIsMember': False,
        }
        return render(request, 'university.html', context)
    return render(request, 'autherror.html')

def getCourseManage(request):
    if request.user.is_authenticated():
        in_university_name = request.GET.get('name', 'None')
        in_university = models.University.objects.get(name__exact=in_university_name)
        in_course_tag = request.GET.get('course', 'None')
        print "course Tag:"
        print in_course_tag
        in_course = in_university.course_set.get(tag__exact=in_course_tag)
        members_list = in_course.members.all()
        context = {
            'university'    : in_university,
            'course'        : in_course,
            'members_list'  : members_list,
        }
        return render(request, 'coursemanage.html', context)
    return render(request, 'autherror.html')

def getCourse(request):
    if request.user.is_authenticated():
	in_university_name = request.GET.get('name', 'None')
	in_university = models.University.objects.get(name__exact=in_university_name)
	in_course_tag = request.GET.get('course', 'None')
	in_course = in_university.course_set.get(tag__exact=in_course_tag)
	is_member = in_course.members.filter(email__exact=request.user.email)
	context = {
	    'university' : in_university,
	    'course' : in_course,
	    'userInCourse' : is_member,
	}
	return render(request, 'course.html', context)
    return render(request, 'autherror.html')

def courseForm(request):
	if request.user.is_authenticated():
		in_university_name = request.GET.get('name', 'None')
		in_university = models.University.objects.get(name__exact=in_university_name)
		context = {
			'university': in_university,
		}
		return render(request, 'courseform.html', context)
    # render error page if user is not logged in
	return render(request, 'autherror.html')

def addCourse(request):
	if request.user.is_authenticated():
		if request.method == 'POST':
			form = forms.CourseForm(request.POST)
			if form.is_valid():
				in_university_name = request.GET.get('name', 'None')
				in_university = models.University.objects.get(name__exact=in_university_name)
				if in_university.course_set.filter(tag__exact=form.cleaned_data['tag']).exists():
					return render(request, 'courseform.html', {'error' : 'Error: That course tag already exists at this university!'})
				new_course = models.Course(tag=form.cleaned_data['tag'],
										   name=form.cleaned_data['name'],
										   description=form.cleaned_data['description'],
										   university=in_university)
				new_course.save()
				in_university.course_set.add(new_course)
				is_member = in_university.members.filter(email__exact=request.user.email)
				context = {
					'university' : in_university,
					'userIsMember': is_member,
				}
				return render(request, 'university.html', context)
			else:
				return render(request, 'courseform.html', {'error' : 'Undefined Error!'})
		else:
			form = forms.CourseForm()
			return render(request, 'courseform.html')
		# render error page if user is not logged in
	return render(request, 'autherror.html')
		
def removeCourse(request):
	if request.user.is_authenticated():
		in_university_name = request.GET.get('name', 'None')
		in_university = models.University.objects.get(name__exact=in_university_name)
		in_course_tag = request.GET.get('course', 'None')
		in_course = in_university.course_set.get(tag__exact=in_course_tag)
		in_course.delete()
		is_member = in_university.members.filter(email__exact=request.user.email)
		context = {
			'university' : in_university,
			'userIsMember' : is_member,
		}
		return render(request, 'university.html', context)
	# render error page if user is not logged in
	return render(request, 'autherror.html')

def addStudentList(request):
    if request.user.is_authenticated():
        in_university_name = request.GET.get('name', 'None')
        in_university = models.University.objects.get(name__exact=in_university_name)
        in_course_tag = request.GET.get('course', 'None')
        in_course = in_university.course_set.get(tag__exact=in_course_tag)
        members_list = in_course.members.all()
        users_list = MyUser.objects.filter(is_student__exact=True)
        context = {
            'university'    : in_university,
            'course'        : in_course,
            'users_list'  : users_list,
        }
        return render(request, 'addstudentlist.html', context)
    return render(request, 'autherror.html')   

def addStudent(request):
    if request.user.is_authenticated():
        in_university_name = request.GET.get('name', 'None')
        in_university = models.University.objects.get(name__exact=in_university_name)
        in_course_tag = request.GET.get('course', 'None')
        in_course = in_university.course_set.get(tag__exact=in_course_tag)
        members_list = in_course.members.all()
        users_list = MyUser.objects.filter(is_student__exact=True)
        in_student_uname = request.GET.get('student', 'None')
        in_student = MyUser.objects.get(uname__exact=in_student_uname)
        in_course.members.add(in_student)
        in_course.save()
        context = {
            'university'    : in_university,
            'course'        : in_course,
            'users_list'    : users_list,
            'student'       : in_student,
        }
        return render(request, 'addstudent.html', context)
    return render(request, 'autherror.html')   
        

def removeStudent(request):
    if request.user.is_authenticated():
        in_university_name = request.GET.get('name', 'None')
        in_university = models.University.objects.get(name__exact=in_university_name)
        in_course_tag = request.GET.get('course', 'None')
        in_course = in_university.course_set.get(tag__exact=in_course_tag)
        members_list = in_course.members.all()
        in_removee = request.GET.get('student', 'None')
        removeeobj = MyUser.objects.get(uname__exact=in_removee)
        try:
            removee = in_course.members.get(uname__exact=in_removee)
            in_course.members.remove(removee)
            in_course.save()
        except:
            removee = None
        context = {
            'course'        : in_course,
            'university'    : in_university,
            'removee'       : removee,
            'removeeobj'    : removeeobj,
        }
        return render(request, 'removestudent.html', context)
    return render(request, 'autherror.html')

def joinCourse(request):
	if request.user.is_authenticated():
		in_university_name = request.GET.get('name', 'None')
		in_university = models.University.objects.get(name__exact=in_university_name)
		in_course_tag = request.GET.get('course', 'None')
		in_course = in_university.course_set.get(tag__exact=in_course_tag)
		in_course.members.add(request.user)
		in_course.save();
		request.user.course_set.add(in_course)
		request.user.save()
		context = {
			'university' : in_university,
			'course' : in_course,
			'userInCourse': True,
		}
		return render(request, 'course.html', context)
	return render(request, 'autherror.html')

def unjoinCourse(request):
	if request.user.is_authenticated():
		in_university_name = request.GET.get('name', 'None')
		in_university = models.University.objects.get(name__exact=in_university_name)
		in_course_tag = request.GET.get('course', 'None')
		in_course = in_university.course_set.get(tag__exact=in_course_tag)
		in_course.members.remove(request.user)
		in_course.save();
		request.user.course_set.remove(in_course)
		request.user.save()
		context = {
			'university' : in_university,
			'course' : in_course,
			'userInCourse': False,
		}
		return render(request, 'course.html', context)
	return render(request, 'autherror.html')
