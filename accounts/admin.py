from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.models import Role, Permission, RolePermission, User, AuditLog, UserWarehouse


class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
    (None, {'fields': ('phone', 'status', 'role')}),
    )
    list_display = ('username', 'email', 'phone', 'status', 'role', 'is_staff')

admin.site.register(Role)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Permission)
admin.site.register(AuditLog)
admin.site.register(RolePermission)
admin.site.register(UserWarehouse)