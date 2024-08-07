from django.db import models
from django.conf import settings

class Account(models.Model):
    address = models.CharField(null=True, max_length=500)
    gender = models.CharField(null=True, max_length=75) 
    auth_user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.firstname} {self.lastname}" 
