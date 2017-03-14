from __future__ import unicode_literals
from django.contrib.auth.models import User 
from django.db import models

class UserProfile(models.Model):  
    user=models.OneToOneField(User,unique=True,verbose_name=('user'))#a******  
    point=models.BigIntegerField(default="0")#b******  

# Create your models here.
# class User(models.Model):
#     username = models.CharField(max_length=50)
#     email = models.EmailField()
#     password = models.CharField(max_length=50)
