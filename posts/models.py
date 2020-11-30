"""Post model"""
#Django

from django.db import models

# Create your models here.
class User(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    is_admin = models.BooleanField(default=False)

    bio = models.TextField(blank=True)
    birthdate = models.DateField(blank=True, null=True)

    country = models.CharField(max_length=25, blank=True)
    city = models.CharField(max_length=50, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
   