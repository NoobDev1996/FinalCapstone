from django.shortcuts import render

"""

This .py file defines the view funtions for handling different pages
of the web app

The index function is responsible for rendering the index page

The homepage functon is responsible for rendering the homepage

The tourdates function is responsible for rendering the tourdates page

These view functions are associated with the URL patterns in the projects URL config.
When a client makes a request to the corresponding URL's the framework will invoke the
respective functions to handle the requests

"""

# Create your views here.
def index(request):
    return render(request, "homepage/index.html")

def homepage(request):
    return render(request, "homepage/homepage.html")

def tourdates(request):
    return render(request, "tourdates/tourdates.html")

