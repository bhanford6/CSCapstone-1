from django import forms

class ProjectForm(forms.Form):
    name = forms.CharField(label="Name", max_length=100)
    start = forms.DateField(label="Start")
    end = forms.DateField(label="End")
    description = forms.CharField(label="Description", max_length=10000)
    knowledge = forms.CharField(label="Knowledge", max_length=10000)
    experience = forms.CharField(label="Experience", max_length=10000)

