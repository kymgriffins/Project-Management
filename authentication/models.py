from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    ROLES_CHOICES = [
        ('manager', 'Manager'),
        ('foreman', 'Foreman'),
        ('architect', 'Architect'),
        ('owner', 'Owner'),
        ('contractor','Contractor')
    ]
    roles = models.CharField(max_length=255, choices=ROLES_CHOICES)
    email = models.EmailField('Email', max_length=255, unique=True)
    
    USERNAME_FIELD ='email'
    REQUIRED_FIELDS = ['username', 'roles']
