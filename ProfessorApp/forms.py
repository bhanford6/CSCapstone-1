from django import forms

class ProfessorForm(forms.Form):
    firstName = forms.CharField(label='firstName', max_length=50)
    lastName = forms.CharField(label='lastName', max_length=50)
