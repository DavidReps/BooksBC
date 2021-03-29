from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    username = forms.CharField(max_length=40, required=True)
    email = forms.CharField(max_length=40, required=True)
    password1 = forms.CharField(max_length=30, required=True)
    password2 = forms.CharField(max_length=30, required=True)


    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

