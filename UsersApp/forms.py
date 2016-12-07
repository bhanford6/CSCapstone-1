from django import forms
from models import Student
class StudentForm(forms.Form):
    
    university = forms.CharField(label='University', max_length=50)
    email = forms.EmailField(label='Email', max_length=255)
    phone = forms.CharField(label='Phone', max_length=16)
    about = forms.CharField(widget=forms.Textarea, label='About', max_length=100000)
    skills = forms.CharField(widget=forms.Textarea, label='Skills', max_length=10000)

class ProfessorForm(forms.Form):
    university = forms.CharField(label='University', max_length=50)
    email = forms.EmailField(label='Email', max_length=255)
    phone = forms.CharField(label='Phone', max_length=16)
    about = forms.CharField(widget=forms.Textarea, label='About', max_length=100000)
    classes = forms.CharField(widget=forms.Textarea, label='Classes', max_length=10000) 

class EngineerForm(forms.Form):
    university = forms.CharField(label='University', max_length=50)
    email = forms.EmailField(label='Email', max_length=255)
    phone = forms.CharField(label='Phone', max_length=16)
    about = forms.CharField(widget=forms.Textarea, label='About', max_length=100000)
    company = forms.CharField(label='Company', max_length=100)
    aboutcomp = forms.CharField(label='About Company', max_length=100000)
    projects = forms.CharField(label='Projects', max_length=10000)
