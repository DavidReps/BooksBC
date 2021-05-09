from django.contrib import admin
from .models import Profile, Book, Message, Report, Sold

admin.site.register(Profile)
admin.site.register(Book)
admin.site.register(Message)
admin.site.register(Report)
admin.site.register(Sold)
