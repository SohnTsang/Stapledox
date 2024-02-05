from django.db import models
from django.utils import timezone
from products.models import Product
from document_types.models import DocumentType

class Document(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='documents')
    document_type = models.ForeignKey(DocumentType, on_delete=models.CASCADE)
    file_name = models.CharField(max_length=255)
    file_path = models.CharField(max_length=255)  # Consider using Django's FileField in actual implementation
    version = models.IntegerField(default=1)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)