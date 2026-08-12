from django.db import models

class Warehouse(models.Model):
    STATUS_CHOICES = (('active', 'active'), ('inactive', 'inactive'))
    code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=50)
    address = models.TextField(blank=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='active', )


