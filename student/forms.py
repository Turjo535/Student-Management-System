
from django import forms
from .models import student_model

class student_model_form(forms.ModelForm):
    class Meta:
        model=student_model
        fields=('name','email','phone','course')

