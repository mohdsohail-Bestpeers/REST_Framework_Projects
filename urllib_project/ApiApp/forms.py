from django import forms
from . models import Student
#from . models import Event


class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'