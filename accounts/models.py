from django.db import models

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
    price = models.DecimalField(max_digits=6, decimal_places=2)
    isbn = models.IntegerField()