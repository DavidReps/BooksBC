from django.contrib import admin
from .models import Profile, Book, Message, Report, Cart, Sold, SearchCount, Rating

admin.site.register(Profile)
admin.site.register(Book)
admin.site.register(Message)
admin.site.register(Report)
admin.site.register(Cart)
admin.site.register(Sold)
admin.site.register(SearchCount)
admin.site.register(Rating)
