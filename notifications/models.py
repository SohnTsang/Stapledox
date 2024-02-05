from django.db import models
from django.utils import timezone
from users.models import User

class Notification(models.Model):
    NOTIFICATION_TYPE_CHOICES = [
        ('Email', 'Email'),
        ('InSite', 'InSite'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    title = models.CharField(max_length=255)
    message = models.TextField()
    status = models.CharField(max_length=6, choices=[('Unread', 'Unread'), ('Read', 'Read')])
    notification_type = models.CharField(max_length=6, choices=NOTIFICATION_TYPE_CHOICES)
    created_at = models.DateTimeField(default=timezone.now)
    deleted_at = models.DateTimeField(null=True, blank=True)