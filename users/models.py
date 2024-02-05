from django.db import models
from django.utils import timezone

class User(models.Model):
    ROLE_CHOICES = [
        ('Exporter', 'Exporter'),
        ('Partner', 'Partner'),
        ('Admin', 'Admin'),
    ]
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password_hash = models.CharField(max_length=128)  # Consider using Django's built-in User model or extend it with AbstractUser for authentication
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)