"""

This .py file contains Django view functions for user authentication and registration.

The views in this file handle the registration, login, and authentication processes for users.

The `register` view handles the registration process when a user submits a registration form.
If the HTTP request method is POST, the function retrieves the submitted username, password, and first name.
It then creates a new user using the `User.objects.create_user` method, passing the provided username,
password, and first name. After creating the user, it logs in the user using the `login` function and redirects
the user to the polls page.

The `user_login` view renders the login form template.

The `authenticate_user` view handles the authentication process when a user submits the login form.
It retrieves the submitted username, password, and first name and attempts to authenticate the user using
the `authenticate` function. If the authentication is successful, the user is logged in using the `login`
function and redirected to the polls page. If the authentication fails, the user is redirected back to the
login page.

The `show_user` view displays the username, first name, and password of the currently authenticated user.
It retrieves this information from the `request.user` object and renders the user.html template.

The `polls_redirect` view redirects the user to the polls page.

"""
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

