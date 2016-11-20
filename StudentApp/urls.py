from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^student/all$', views.getStudents, name='Students'),
    url(r'^student/form$', views.getStudentForm, name='StudentForm'),
    url(r'^student$', views.getStudent, name='Student'),
]
