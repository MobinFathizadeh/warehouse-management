from django.db import models

class Warehouse(models.Model):
    STATUS_CHOICES = (('active', 'active'), ('inactive', 'inactive'))
    code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=50)
    address = models.TextField(blank=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='active', )



class Location(models.Model):
    TYPE_CHOICES = (('zone', 'Zone'), ('aisle', 'Aisle'), ('shelf', 'Shelf'), ('bin', 'Bin'))

    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, related_name='locations')
    parent = models.ForeignKey('self', on_delete=models.PROTECT, null=True, blank=True, related_name='children')
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50, choices=TYPE_CHOICES)

    class Meta:
        unique_together = ('warehouse', 'code')
