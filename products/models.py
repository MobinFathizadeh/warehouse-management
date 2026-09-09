from django.db import models

class Category(models.Model):
    parent = models.ForeignKey('self', on_delete=models.PROTECT, null=True, blank=True, related_name='children')
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)


class Product(models.Model):
    STATUS_CHOICES = (('active', 'Active'), ('discontinued', 'Discontinued'))
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True, blank=True, related_name='products')
    sku = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    barcode = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    unit = models.CharField(max_length=100)
    status = models.CharField(max_length=100, choices= STATUS_CHOICES, default='active')



class Supplier(models.Model):
    STATUS_CHOICES = (('active', 'Active'), ('inactive', 'Inactive'))

    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=15)
    address = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')



class Customer(models.Model):
    STATUS_CHOICES = (('active', 'Active'), ('inactive', 'Inactive'))

    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=15)
    address = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')

