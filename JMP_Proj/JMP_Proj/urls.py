"""
URL configuration for JMP_Proj project.

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
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

urlpatterns = [
    path('', include('JMP_App.urls')),
    path('admin/', admin.site.urls), 
    path('accounts/', include('allauth.urls')),
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('accounts/login', TemplateView.as_view(template_name='accounts/login.html'), name='login'),
    path('accounts/signup', TemplateView.as_view(template_name='accounts/signup.html'), name='signup'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
]   
