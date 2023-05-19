"""
This .py file defines the URL configuration for the 'contact' app in my Django project.

The `urlpatterns` list is a collection of URL patterns associated with view functions or classes.
In this case, there is a single URL pattern defined for the 'contact' app. It maps the root URL
(path '') to the `contact_view` function from the `views` module. The name of this URL pattern
is set as 'contact'.

The `app_name` variable defines the namespace for the 'contact' app. It helps in resolving URL
names when multiple apps have URL patterns with the same name.

"""
from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'contact'
urlpatterns = [
    path('', views.contact_view, name='contact'),
]