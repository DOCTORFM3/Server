"""Texter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from Profiles import views

urlpatterns = [
    path('view/<username>', views.Profile_Page, name = 'profile_view'),
    path('edit/<username>', views.Edit_Profile_Page, name = 'profile_edit'),
    path('login', views.Login, name = 'login'),
    path('logout', views.Logout, name = 'logout'),
    path('register', views.Register, name = 'register'),
]
