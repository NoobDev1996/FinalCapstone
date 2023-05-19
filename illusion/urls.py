"""
URL configuration for illusion project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from polls.views import detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tourdates/', include('tourdates.urls', namespace ='tourdates')),
    path('homepage/', include('homepage.urls', namespace='homepage')),
    path('contact/', include('contact.urls', namespace='contact')),
    path('polls/', include('polls.urls', namespace='polls')),
    path('polls/<int:question_id>/', detail, name='detail'),
    path('user_auth/', include(("django.contrib.auth.urls", 'registration'))),
    path('user_path/', include("user_auth.urls")),

]
