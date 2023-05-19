"""
This .py file defines a Django view function for handling a contact page request

The contact_view is responsible for rendering the contact page
it takes a request object as a parameter which represents the HTTP
request made by a client. The function uses the 'render' function from the 'django.shortcuts
module to generate an HTTP response with the rendered HTML template.

"""

from django.shortcuts import render

# Create your views here.
def contact_view(request):
    return render(request, "contact/contact.html")