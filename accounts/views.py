from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import RegistrationForm, ClientCreationForm
from django.contrib.auth import authenticate, login, logout

#edit
def register(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegistrationForm(request.POST or None)

        # check whether it's valid:
        if form.is_valid():
            user = form.save()

            # process the data in form.cleaned_data as required
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username = user.username, password=raw_password)

            #log the user in to the system
            login(request, user)


            # redirect to a new URL:
            #this is just to confirm to the client that the form has been sumbited succesfully
            return HttpResponseRedirect('/clientcreation/')

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

            # # process the data in form.cleaned_data as required
            # raw_password = form.cleaned_data.get('password1')
            # user = authenticate(username = user.username, password=raw_password)

            # #log the user in to the system
            # login(request, user)


            # redirect to a new URL:
            #this is just to confirm to the client that the form has been sumbited succesfully
            return HttpResponseRedirect('/clientcreation/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ClientCreationForm()

    return render(request, 'accounts/clientcreation.html', {'form': form})



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



