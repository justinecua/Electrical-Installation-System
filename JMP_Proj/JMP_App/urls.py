from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('signup/', views.signup, name="signup"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('validatelogin/', views.validatelogin, name="login"),
    path('adminpanel/', views.adminpanel, name="adminpanel"),
    path('adminAccounts/', views.adminAccounts, name="adminAccounts"),
    path('adminServices/', views.adminServices, name="adminServices"),
    path('adminProjects/', views.adminProjects, name="adminProjects"),
    path('adminPayments/', views.adminPayments, name="adminPayments"),
    path('adminServices/saveService/', views.saveService, name="saveService"),
    path('adminServices/deleteService/<int:serviceId>', views.deleteService, name="deleteService"),
    path('adminServices/fetch4editService/<int:serviceId>', views.fetch4editService, name="fetch4editService"),
    path('adminProjects/saveProject/', views.saveProject, name="saveProject"),
    path('adminProjects/editProject/', views.editProject, name='editProject'),
    path('adminProjects/delete_project/<int:project_id>/', views.deleteProject, name='deleteProject'),
]
