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
    roles = models.ManyToManyField(Role, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def save(self, *args, **kwargs):
        created = not self.pk  # Check if the user is being created
        super().save(*args, **kwargs)

        if created:
            # Create a default role for the user if it's a new user
            default_role, _ = Role.objects.get_or_create(name='user')
            self.roles.add(default_role)

