from django.db import models
from django.contrib.auth.models import AbstractUser

class Role(models.Model):
    name = models.CharField(max_length=255, unique=True)
    permissions = models.ManyToManyField("Permission", blank=True)

    def __str__(self):
        return self.name

class Permission(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name

class User(AbstractUser):
    email = models.EmailField('Email', max_length=255, unique=True)
    # roles = models.ManyToManyField(Role, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

   