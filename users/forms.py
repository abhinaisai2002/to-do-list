from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.forms import fields
from django.db import models

class UserCreateForm(UserCreationForm):
    email = forms.EmailField()
    firstname = forms.CharField(max_length=20)
    lastname = forms.CharField(max_length=20)
    class Meta:
        model = User
        fields = ['username','firstname','lastname','email','password1','password2']


class LoginForm(AuthenticationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
