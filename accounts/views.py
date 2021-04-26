from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import RegistrationForm, ClientCreationForm, BookSellerForm
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

#edit
def register(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegistrationForm(request.POST or None)

        # check whether it's valid:
        if form.is_valid():
            email = request.POST.get('username')
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
            user = form.save()


            # redirect to a new URL:
            #this is just to confirm to the client that the form has been sumbited succesfully
            return HttpResponseRedirect(reverse('accounts:home'))
    # if a GET (or any other method) we'll create a blank form
    else:
        form = ClientCreationForm()

    return render(request, 'accounts/clientcreation.html', {'form': form})

def log_in(request):
    if request.method == 'POST':

        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)
            login(request, user)
            return HttpResponseRedirect('/buying')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def log_out(request):
    logout(request)
    return HttpResponseRedirect('/login')

# def sellerlisting(request):
#     if request.method == 'POST':
#         # create a form instance and populate it with data from the request:
#         form = BookSellerForm(request.POST or None)

#         # check whether it's valid:
#         if form.is_valid():
#             print("VALID")
#             # photo = request.FILES['photo']
#             # photo.save()

#             user = form.save()


#             # redirect to a new URL:
#             #this is just to confirm to the client that the form has been submitted succesfully
#             return HttpResponseRedirect(reverse('accounts:home'))
#         else:
#             print("INVALID")

#     # if a GET (or any other method) we'll create a blank form
#     else:

#         form = BookSellerForm()

#     return render(request, 'accounts/sellerlisting.html', {'form': form})

def cart(request):

    return render(request, 'accounts/cart.html')

def profile(request):

    return render(request, 'accounts/profile.html')

def sellerlisting(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = BookSellerForm(request.POST, request.FILES or None)

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


            obj = Book.objects.create(
                                 title = title, 
                                 author = author,
                                 edition = edition,
                                 condition = condition,
                                 course = course,
                                 image = image,
                                 price = price,
                                 isbn = isbn,
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
        #allBooks = None
        search_choice = request.GET.get('filter')
        submitbutton= request.GET.get('submit')
        if query is not None:
            if search_choice == "Title":
                allBooks =  Book.objects.filter(Q(title__icontains=query)).order_by('price')
                context={'books' :allBooks,
                     'sumbitbutton': submitbutton}
                return render(request, 'accounts/index.html', context)
            if search_choice == "Author":
                allBooks =  Book.objects.filter(Q(author__icontains=query)).order_by('price')
                context={'books' :allBooks,
                     'sumbitbutton': submitbutton}
                return render(request, 'accounts/index.html', context)
            if search_choice == "isbn":
                allBooks =  Book.objects.filter(Q(isbn__istartswith=query)).order_by('price')
                context={'books' :allBooks,
                     'sumbitbutton': submitbutton}
                return render(request, 'accounts/index.html', context)
            if search_choice == "Course":
                allBooks =  Book.objects.filter(Q(course__icontains=query)).order_by('price')
                context={'books' :allBooks,
                     'sumbitbutton': submitbutton}
                return render(request, 'accounts/index.html', context)
            else:
                allBooks = Book.objects.all()
                context = {
                    'books' :allBooks,
                }
                return render(request, 'accounts/index.html', context)
        else:
            allBooks = Book.objects.all()
            context = {
                'books' :allBooks,
            }
            return render(request, 'accounts/index.html', context)
            return render(request, 'accounts/index.html',)
    else:
        return render(request, 'accounts/index.html')

def home(request):
    return render(request, 'accounts/base.html')

# def home(request):
#     query = request.GET.get("title")
#     allMovies = None

#     if query:
#         allMovies = Movie.objects.filter(name__icontains=query)
#     else:
#         allMovies = Movie.objects.all()

#     context = {
#         "movies": allMovies,
#     }

#     return render(request,'main/index.html', context)


# def login_user(request):
#     if request.user.is_authenticated:
#         return redirect("main:home")
#     else:
#         if request.method == "POST":
#             username = request.POST['username']
#             password = request.POST['password']

#             user = authenticate(username=username, password=password)

#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#                     return redirect("main:home")

#                 else:
#                     return render(request, 'accounts/login.html', {"error": "your account has ben disabled."})

#             else:
#                 return render(request, 'accounts/login.html', {"error": "sorry chief, invalid username or password."})

#         return render(request, 'accounts/login.html')



