from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import RegistrationForm, ClientCreationForm, BookSellerForm, ReportForm, AddToCartForm, SoldBookForm, AddToSearchForm, RatingForm
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q, Avg
from django.contrib import messages
from django.utils.safestring import mark_safe
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.db.models import F
import json
import random

def rating(request):
    
    if request.method == 'POST':
        form = RatingForm(request.POST or None)

        if form.is_valid():
            toBeRated = form.cleaned_data.get('message')
            score = form.cleaned_data.get('rating')

            print(score, toBeRated)


def sold_book(request, bookId):

    if request.method == 'POST':
        form = SoldBookForm(request.POST or None)

        if form.is_valid():
            count = form.cleaned_data.get('count')

            sold, created = Sold.objects.get_or_create(bookName=bookId, count=count)

            sold.save()
            
            #if already created we know one other user has claimed the book has sold
            if created is False:
                soldBook = Book.objects.get(bookId=bookId)
                soldBook.delete()
        else:
            print('-----------------------form  is not valid------------------------------')
        return HttpResponseRedirect('/rating.html')
    else:
        form = SoldBookForm()

    return render(request, 'accounts/sold.html', {'form': form})


def register(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegistrationForm(request.POST or None)

        # check whether it's valid:
        if form.is_valid():
            email = request.POST.get('username')

            #check if bc email is being used
            if "bc.edu" not in email:
                messages.error(request, 'ERROR: Please use a valid BC email address')
                return render(request, 'accounts/register.html', {'form': form})
            
            user = form.save()

            # process the data in form.cleaned_data as required
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username = user.username, password=raw_password)

            #log the user in to the system
            login(request, user)


            # redirect to a new URL:
            #this is just to confirm to the client that the form has been sumbited succesfully
            return HttpResponseRedirect('/clientcreation')
        else:
            messages.error(request, "ERROR: Please make sure your passwords match")


    # if a GET (or any other method) we'll create a blank form
    else:
        form = RegistrationForm()

    return render(request, 'accounts/register.html', {'form': form})

def clientcreation(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ClientCreationForm(request.POST or None)

        # check whether it's valid:
        if form.is_valid():
            email = request.POST.get('email')

            #check if bc email is being used
            if "bc.edu" not in email:
                messages.error(request, 'ERROR: Please use a valid BC email address')
                return render(request, 'accounts/clientcreation.html', {'form': form})

            #check if passwords match
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')
            if password1 != password2:
                messages.error(request, 'ERROR: Make sure passwords match')
                return render(request, 'accounts/clientcreation.html', {'form': form})

            user = form.save()


            # redirect to a new URL:
            #this is just to confirm to the client that the form has been sumbited succesfully
            return HttpResponseRedirect(reverse('accounts:home'))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ClientCreationForm()

    return render(request, 'accounts/clientcreation.html', {'form': form})

def log_in(request):
     # if this is a POST request we need to process the form data
    if request.method == 'POST':

        # create a form instance and populate it with data from the request:
        form = AuthenticationForm(data=request.POST)

        # check whether it's valid
        if form.is_valid():
            username = request.POST.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)

            #log the user in to the system
            login(request, user)

            # redirect to buying url to show success:
            return HttpResponseRedirect('/buying')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def log_out(request):
    logout(request)
    return HttpResponseRedirect('/login')


def chat(request):
    return render(request, 'accounts/chat.html',{
        'username': mark_safe(json.dumps(request.user.username)),

    })

@login_required
def room(request, room_name, bookId):
    # creator = Book.objects.get(bookId=bookId).values('createdBy')
    # creator = Book.objects.values_list('createdBy', flat=True).get(bookId=bookId)

    return render(request, 'accounts/room.html', {
        'room_name': room_name,
        'username': mark_safe(json.dumps(request.user.username)),
        'bookId': bookId,
        # 'creator':creator,
    })

@login_required
def add_to_cart(request):
    key_a = request.GET['book_isbn']
    book = Book.objects.get(isbn=key_a)
    current_user = request.user
    user = current_user.username

    if request.method == 'POST':
        form = AddToCartForm(request.POST, request.FILES or None, initial = {'book': book,'user': "none"})
        if form.is_valid():
            current_user = request.user
            user = current_user.username

            obj = Cart.objects.create(
                                        book = book, 
                                        user = user,
            )
            obj.save()
        else:
            print("FORM IS NOT VALID")
    else:
        form = BookSellerForm()
        print("REQUEST IS NOT POST")

    return HttpResponseRedirect(reverse('accounts:cart'))


def cart(request):
    allCarts = Cart.objects.all()
    username = request.user.username
    context = {
        'carts' :allCarts,
        'username': username,
    }

    return render(request, 'accounts/usercart.html', context)

def profile(request, user):
    currentUser = Profile.objects.get(email=user)

    buyerRate = currentUser.buyer_rating
    sellerRate = currentUser.seller_rating
    n = currentUser.ratings

    if n ==0:
        n = n+1
    averageSeller = sellerRate//n
    averageBuyer = buyerRate//n



    context={
        'user': currentUser,
        'sellerAverage':averageSeller,
        'buyerAverage':averageBuyer,
    }


    return render(request, 'accounts/profile.html', context)


def sellerlisting(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = BookSellerForm(request.POST, request.FILES or None, initial = {'createdBy': "none"})

        # check whether it's valid:
        if form.is_valid():
            #fields = ('title', 'author', 'edition', 'condition', 'course', 'image', 'price', 'isbn')
            title = form.cleaned_data.get('title')
            author = form.cleaned_data.get('author')
            edition = form.cleaned_data.get('edition')
            condition = form.cleaned_data.get('condition')
            course = form.cleaned_data.get('course')
            image  = request.FILES['image']
            #IMAGESTUFF - line above
            price = form.cleaned_data.get('price')
            isbn = form.cleaned_data.get('isbn')
            
            

            current_user = request.user
            createdBy = current_user.username[0:-7]

            random_number = random.randint(0,16777215)
            
            random_number2 = random.randint(0,random_number)

            bookId = random_number2

            obj = Book.objects.create(
                                 title = title, 
                                 author = author,
                                 edition = edition,
                                 condition = condition,
                                 course = course,
                                 image = image,
                                 price = price,
                                 isbn = isbn,
                                 createdBy = createdBy,
                                 bookId = bookId,
            )
            obj.save()


            # redirect to a new URL:
            #this is just to confirm to the client that the form has been sumbited succesfully
            return HttpResponseRedirect(reverse('accounts:home'))
    # if a GET (or any other method) we'll create a blank form
    else:
        form = BookSellerForm()

    return render(request, 'accounts/sellerlisting.html', {'form': form})

def buying(request):
    if request.method == 'GET':
        query= request.GET.get('q')
        
        #create filter for search bar
        filter_selection = request.GET.get('filter')
        searchbutton= request.GET.get('submit')
        if query is not None:
            
            #filter options of Title, Author, ISBN, and Course
            if filter_selection == "Title":
                #filter by title and order by price lowest to highest
                allBooks =  Book.objects.filter(Q(title__icontains=query)).order_by('price')
                context={
                    'books' :allBooks,
                    'sumbitbutton': searchbutton,
                    'username': request.user.username[0:-7],
                }
                return render(request, 'accounts/index.html', context)
            
            if filter_selection == "Author":
                #filter by author and order by price lowest to highest
                allBooks =  Book.objects.filter(Q(author__icontains=query)).order_by('price')
                context={
                    'books' :allBooks,
                    'sumbitbutton': searchbutton,
                    'username': request.user.username[0:-7],
                }
                return render(request, 'accounts/index.html', context)
            
            if filter_selection == "isbn":
                #filter by ISBN and order by price lowest to highest
                allBooks =  Book.objects.filter(Q(isbn__istartswith=query)).order_by('price')
                context={
                    'books' :allBooks,
                    'sumbitbutton': searchbutton,
                    'username': request.user.username[0:-7],
                }
                return render(request, 'accounts/index.html', context)
            
            if filter_selection == "Course":
                #filter by Course and order by price lowest to highest
                allBooks =  Book.objects.filter(Q(course__icontains=query)).order_by('price')
                context={
                    'books' :allBooks,
                    'sumbitbutton': searchbutton,
                    'username': request.user.username[0:-7],

                    }
                return render(request, 'accounts/index.html', context)
            
            else:
                #show all books
                allBooks = Book.objects.all()
                context = {
                    'books' :allBooks,
                    'username': request.user.username[0:-7],

                }
                return render(request, 'accounts/index.html', context)
        else:
            #show all books
            allBooks = Book.objects.all()
            context = {
                'books' :allBooks,
                'username': request.user.username[0:-7],
            }
            return render(request, 'accounts/index.html', context)
    else:
        return render(request, 'accounts/index.html')

def adminpage(request):
    user_count= Profile.objects.all().count()
    total_searches = SearchCount.objects.all().count()

    context= {'user_count': user_count,
                'total_searches': total_searches}
    return render(request, 'accounts/adminindex.html', context)

def reportlisting(request):
    key_a = request.GET['book_id']
    book = Book.objects.get(bookId=key_a)
    seller = book.createdBy


    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ReportForm(request.POST or None, initial = {'createdBy': "none", 'book': book, 'seller': seller})

        # check whether it's valid:
        if form.is_valid():
            #fields = ('message', 'createdBy')
            message = form.cleaned_data.get('message')

            current_user = request.user
            createdBy = current_user.username

            obj = Report.objects.create(
                message = message, 
                createdBy = createdBy,
                book = book,
                seller = seller,
            )
            obj.save()


            # redirect to a new URL:
            #this is just to confirm to the client that the form has been sumbited succesfully
            return HttpResponseRedirect(reverse('accounts:buying'))
    # if a GET (or any other method) we'll create a blank form
    else:
        form = ReportForm()

    return render(request, 'accounts/reportlisting.html', {'form': form})


def home(request):
    return render(request, 'accounts/base.html')
