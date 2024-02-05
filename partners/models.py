from django.db import models
from django.utils import timezone
from users.models import User

class Partner(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),
    ]
    exporter_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='exporter_partners')
    partner_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='partner_partners')
    status = models.CharField(max_length=8, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)