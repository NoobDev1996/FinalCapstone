from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.urls import reverse


# Create your views here.

def register(request):
     if request.method=='POST':
          username = request.POST['username']
          password = request.POST['password']
          first_name = request.POST['first_name']

          # Create a new user
          user = User.objects.create_user(username=username, password=password, first_name=first_name)

          #Log in the user
          login(request, user)

          # Redirect to the polls page
          return redirect(reverse('user_auth:polls_redirect'))
     
     return render(request, 'registration/register.html')


def user_login(request):
    return render(request, 'registration/login.html')

def authenticate_user(request):
        username = request.POST['username']
        password = request.POST['password']
        first_name = request.POST['first_name']
        user = authenticate(username=username, password=password, first_name=first_name)
        if user is None:
            return redirect(reverse('user_auth:login'))

        else:
            login(request, user)
            return redirect(reverse('user_auth:polls_redirect'))
        # user_auth:show_user

def show_user(request):
    print(request.user.username)
    return render(request, 'registration/user.html', {
        "username": request.user.username,
        "first_name": request.user.first_name,
        "password": request.user.password
    })

def polls_redirect(request):
    return redirect('polls:index')

