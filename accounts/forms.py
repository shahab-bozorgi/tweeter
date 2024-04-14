from django import forms
from django.contrib.auth import authenticate
from django.forms import ValidationError, TextInput
from django.contrib.auth.models import User



class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password']
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control", "style": "background:rgb(22, 22, 22); padding: 1em;"}),
            "last_name": forms.TextInput(attrs={"class": "form-control", "style": "background:rgb(22, 22, 22); padding: 1em;"}),
            "email": forms.EmailInput(attrs={"class": "form-control", "style": "background:rgb(22, 22, 22); padding: 1em;"}),
            "username": forms.TextInput(attrs={"class": "form-control", "style": "background:rgb(22, 22, 22); padding: 1em;"}),
            "password": forms.PasswordInput(attrs={"class": "form-control", "style": "background:rgb(22, 22, 22); padding: 1em;"}),

        }



