from django.db import models
from django.conf import settings

class Account(models.Model):
    address = models.CharField(null=True, max_length=500)
    gender = models.CharField(null=True, max_length=75) 
    auth_user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.firstname} {self.lastname}"

class Services(models.Model):
    name = models.CharField(null=True, max_length=150)
    description = models.CharField(null=True, max_length=500)
    icon = models.URLField(verbose_name="File Url")
    icon_file_id = models.CharField(max_length=255, null=True, blank=True)
    price = models.CharField(null=True, max_length=50)
    date = models.DateTimeField(auto_now_add=True, null=True, max_length=75)
    
    def __str__(self):
        return f"{self.name}"

class Projects(models.Model):
    caption = models.CharField(null=True, max_length=950) 
    project_picture = models.URLField(verbose_name="File Url")
    project_picture_id = models.CharField(max_length=255, null=True, blank=True) 
    date = models.DateTimeField(auto_now_add=True, null=True, max_length=75)
    
    def __str__(self):
        return f"{self.caption}"
