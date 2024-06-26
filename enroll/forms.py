from django.core import validators
from django import forms
from .models import user


class StudentRegistration(forms.ModelForm):
    class Meta:
        model= user
        fields = ["name", 'email', 'password']
        widgets = {
                'name': forms.TextInput(attrs={'class':"form-control"}),
                'email': forms.EmailInput(attrs={'class':"form-control"}),
                'password': forms.PasswordInput(attrs={'class':"form-control"}),



        }