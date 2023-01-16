from django.db import models
from authentication.models import User
# Create your models here.

class Project(models.Model):
    STATUS_CHOICES = (
        ('inprogress', 'In Progress'),
        ('pending', 'Pending'),
        ('completed', 'Completed'),
    )
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=500)
    scope = models.TextField(max_length=500)
    start_date = models.DateField(blank=True)
    end_date = models.DateField(blank=True)
    status = models.CharField(max_length=255, choices=STATUS_CHOICES)
    current_budget = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    estimated_budget = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    
    
class Team(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    members = models.ManyToManyField(User, related_name='teams')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    
    
class Task(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('inprogress', 'In Progress'),
        ('on-hold', 'On Hold'),
        ('completed', 'Completed'),
    )
    PRIORITY_CHOICES = (
        ('high', 'High'),
        ('medium', 'Medium'),
        ('low', 'Low'),
    )
    project_id = models.ForeignKey(Project, on_delete= models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    priority = models.CharField(max_length=255,choices=PRIORITY_CHOICES, blank=True)
    planned_start_date = models.DateField(blank=False)
    planned_end_date = models.DateField(blank=False)
    actual_start_date = models.DateField(blank=True)
    actual_end_date = models.DateField(blank=True)
    planned_budget = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    current_expense = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    status = models.CharField(max_length=255, choices=STATUS_CHOICES)
    documents = models.FileField(upload_to='docs/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
