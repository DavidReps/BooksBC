from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from .models import Book, Report, Cart


class RegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=40, required=True, widget=forms.TextInput(attrs={'class': "form-row"}))
    password1 = forms.CharField(max_length=30, required=True)
    password2 = forms.CharField(max_length=30, required=True)
    
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

class ClientCreationForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2', 'major', 'completed_courses', 'housing_location')

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ('message', 'createdBy')

    def __init__(self, *args, **kwargs): 
        super(ReportForm, self).__init__(*args, **kwargs)                       
        self.fields['createdBy'].disabled = True

class AddToCartForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = ('book', 'user')
    def __init__(self, *args, **kwargs): 
        super(AddToCartForm, self).__init__(*args, **kwargs)                       
        self.fields['book'].disabled = True
        self.fields['user'].disabled = True

class BookSellerForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'author', 'edition', 'condition', 'course', 'image', 'price', 'isbn', 'createdBy')

    def __init__(self, *args, **kwargs): 
        super(BookSellerForm, self).__init__(*args, **kwargs)                       
        self.fields['createdBy'].disabled = True