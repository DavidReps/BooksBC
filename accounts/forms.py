from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from .models import Book, Report, Sold, Cart, SearchCount, TotalBooksCount, Rating


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
        fields = ('first_name', 'last_name', 'year', 'email', 'password1', 'password2', 'major', 'major2', 'completed_courses', 'housing_location', 'buyer_rating', 'seller_rating')

    def __init__(self, *args, **kwargs): 
        super(ClientCreationForm, self).__init__(*args, **kwargs)                       
        self.fields['buyer_rating'].disabled = True
        self.fields['seller_rating'].disabled = True
        
class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ('book', 'message', 'createdBy', 'seller')

    def __init__(self, *args, **kwargs): 
        super(ReportForm, self).__init__(*args, **kwargs)                       
        self.fields['book'].disabled = True          
        self.fields['createdBy'].disabled = True
        self.fields['seller'].disabled = True

class BookSellerForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'author', 'edition', 'condition', 'course', 'image', 'price', 'isbn', 'createdBy')

    def __init__(self, *args, **kwargs): 
        super(BookSellerForm, self).__init__(*args, **kwargs)                       
        self.fields['createdBy'].disabled = True


class AddToCartForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = ('book', 'user')
    def __init__(self, *args, **kwargs): 
        super(AddToCartForm, self).__init__(*args, **kwargs)                       
        self.fields['book'].disabled = True
        self.fields['user'].disabled = True

class SoldBookForm(forms.ModelForm):
    class Meta:
        model = Sold
        fields = ('bookName', 'count')

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ('message', 'rating')

class AddToSearchForm(forms.ModelForm):
    class Meta:
        model = SearchCount
        fields = ['count']
    def __init__(self, *args, **kwargs): 
        super(AddToSearchForm, self).__init__(*args, **kwargs)                       
        self.fields['count'].disabled = True

class AddToBookForm(forms.ModelForm):
    class Meta:
        model = TotalBooksCount
        fields = ['count']
    def __init__(self, *args, **kwargs):
        super(AddToBookForm, self).__init__(*args, **kwargs)
        self.fields['count'].disabled = True 