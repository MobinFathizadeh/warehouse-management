from django.db import models
from django.contrib.auth.models import AbstractUser


class Role(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)


class Permission(models.Model):
    code = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)

class RolePermission(models.Model):
    permission = models.ForeignKey(Permission, on_delete = models.CASCADE, related_name='permission_roles')
    role = models.ForeignKey(Role, on_delete = models.CASCADE, related_name='role_permissions')
    class Meta:
        unique_together = ('permission', 'role')


class User(AbstractUser):
    STATUS_CHOICES = [
        ('active', 'active'),
        ('inactive', 'inactive'),
        ('suspended', 'suspended'),
    ]
    phone = models.CharField(max_length=13 , unique= True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='active')
    role = models.ForeignKey(Role, on_delete= models.PROTECT, related_name='users')

class AuditLog(models.Model):
    user = models.ForeignKey(User, on_delete = models.SET_NULL, related_name= 'audit_logs', null=True)
    action = models.CharField(max_length=50)
    model_name = models.CharField(max_length=50)
    object_id = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)

class UserWarehouse(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name= 'user_warehouses')
    warehouse = models.ForeignKey('warehouses.Warehouse', on_delete = models.CASCADE, related_name= 'warehouse_users')

    class Meta:
        unique_together = ('user', 'warehouse')