from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class RegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=40, required=True)
    password1 = forms.CharField(max_length=30, required=True)
    password2 = forms.CharField(max_length=30, required=True)
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

class ClientCreationForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2', 'major', 'completed_courses', 'housing_location')


