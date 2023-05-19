"""

This .py file registers the `Question` and `Choice` models with the Django admin site.

The Django admin site provides a web-based interface for managing and interacting with the models in the application.
By registering the models with the admin site, administrators can perform various administrative tasks such as
creating, editing, and deleting instances of the models.

The `Question` and `Choice` models are imported from the `.models` module. They represent the question and choice
objects in the polling application. By registering these models using the `admin.site.register` method, Django
will generate default admin views and forms for managing these models.

"""

from django.contrib import admin
from .models import Question, Choice
# Register your models here.
admin.site.register(Question)
admin.site.register(Choice)