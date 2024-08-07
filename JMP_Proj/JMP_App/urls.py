from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('signup/', views.signup, name="signup"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('validatelogin/', views.validatelogin, name="login"),
    path('adminpanel/', views.adminpanel, name="adminpanel")
]
