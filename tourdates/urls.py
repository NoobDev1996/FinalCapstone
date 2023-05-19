from django.urls import path
from . import views

app_name = 'tourdates'

urlpatterns = [
    path('', views.tourdates_view, name='tourdates'),
]