from dataclasses import field
from django import forms
from .models import Student
from django import views

class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'
        # fields=('Name','Email','Cell','Department','Gender','Picture','YourMessage')