from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Profile(models.Model):

    username = models.CharField(max_length=40)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    password1 = models.CharField(max_length=30)
    password2 = models.CharField(max_length=30)
    major = models.CharField(max_length=30)
    completed_courses = models.CharField(max_length=200)
    housing_location = models.CharField(max_length=30)

class Book(models.Model):

    title = models.CharField(max_length=40)
    author = models.CharField(max_length=40)
    edition = models.CharField(max_length=40)
    condition = models.CharField(max_length=40)
    course = models.CharField(max_length=40)
    image = models.ImageField(upload_to = 'images/', default = 'default.png')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    isbn = models.IntegerField()
    createdBy = models.CharField(max_length=40)

class Cart(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.CharField(max_length=40)


User = get_user_model()

class Message(models.Model):
    
    author = models.ForeignKey(User, related_name='author_messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add = True)
    room = models.CharField(max_length=100, default='')


    def __str__(self):
        return self.author.username

class TotalSearches(models.Model):
    total_searches = models.IntegerField(default=0)

    