from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Musician(models.Model):
    
    #We extend Django’s built-in authentication system that already has things like 
    #userName, email, password, etc, and just extend it with the Musician's profile fields
    #https://docs.djangoproject.com/en/1.8/topics/auth/customizing/#extending-the-existing-user-model
    
    #this extends the User class, so a Musician is a User
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #we might want to use a package for countries/cities, for now leaving as text https://djangopackages.org/grids/g/countries/
    country = models.CharField(max_length=128)
    city = models.CharField(max_length=128)
    
    
    
        