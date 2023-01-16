from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    roles = models.CharField(max_length=255, choices=[('manager', 'manager'), ('member', 'member'),('owner', 'owner')])
    username = models.CharField('Name',max_length=255)
    email = models.EmailField('Email',max_length=255, unique=True)
    password = models.CharField('Password',max_length=255)
    
     
    USERNAME_FIELD ='email'
    REQUIRED_FIELDS =[ 'username', 'roles']