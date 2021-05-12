from django.db import models
from django.contrib.auth import get_user_model
import uuid
from .choices import *

# Create your models here.
class Profile(models.Model):

    username = models.CharField(max_length=40)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    year = models.CharField(max_length=4,default="")
    email = models.CharField(max_length=30)
    password1 = models.CharField(max_length=30)
    password2 = models.CharField(max_length=30)
    major = models.CharField(max_length=30)
    major2 = models.CharField(max_length=30,default="")
    completed_courses = models.CharField(max_length=200)
    housing_location = models.CharField(max_length=30)
    buyer_rating = models.IntegerField(max_length=1,default=0)
    seller_rating = models.IntegerField(max_length=1,default=0)
    buyer_count = models.IntegerField(default=0)
    seller_count = models.IntegerField(default=0)
    average_buyer = models.FloatField(default=0.0)
    average_seller = models.FloatField(default=0.0)

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
    sellerLink = models.CharField(max_length=40, default='')
    bookId = models.CharField(
         max_length=40,
         primary_key = True,
         default = 0,
         editable = False)

class Cart(models.Model):
    book = models.ForeignKey(Book, unique=True, on_delete=models.CASCADE)
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

class Report(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    message = models.CharField(max_length = 100)
    createdBy= models.CharField(max_length=40)
    seller = models.CharField(max_length=40)

class Sold(models.Model):
    bookName = models.CharField(max_length=40)
    count = models.IntegerField(default=0)

class SearchCount(models.Model):
    count = models.IntegerField(default=0)

class TotalBooksCount(models.Model):
    count = models.IntegerField(default=0)

class Rating(models.Model):
    relevance = models.IntegerField(choices=RELEVANCE_CHOICES, default=1)
    rating = models.IntegerField()