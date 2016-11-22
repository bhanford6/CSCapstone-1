from django import forms

class UserForm(forms.Form):
    first_name = forms.CharField(label='first_name', max_length=50)
    last_name = forms.CharField(label='last_name', max_length=50)
    university = forms.CharField(label='University', max_length=50)
    email = forms.EmailField(label='Email', max_length=255)
    phone = forms.CharField(label='Phone', max_length=16)
    about = forms.CharField(label='About', max_length=100000)
    skills = forms.CharField(label='Skills', max_length=10000)
    projects = forms.CharField(label='Projects', max_length=10000)
    aboutcomp = forms.CharField(label='About Copany', max_length=100000)
