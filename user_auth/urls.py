from django.db import models

# Create your models here.
from django.urls import path, include
from .import views

app_name = 'user_auth'
urlpatterns = [
    path('', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path('show_user/', views.show_user, name='show_user'),
    path('authenticate_user/', views.authenticate_user, name="authenticate_user"),
    path('polls/', views.polls_redirect, name='polls_redirect'),
]