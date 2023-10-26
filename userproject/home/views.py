from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout


# Create your views here.

def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, 'index.html')

# from django.views.decorators.csrf import csrf_exempt

# @csrf_exempt
def loginUser(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # check if user has entered correct credentials
        user = authenticate(username=username, password=password)
        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect("/")
    
        else:
            # No backend authenticated the credentials
             return render(request, 'login.html')
            # return HttpResponse('NOT FOUND')

    return render(request, 'login.html')


def logoutUser(request):
    logout(request)
    return redirect("/login")


def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')


def signup(request):
    return render(request,'signup.html')