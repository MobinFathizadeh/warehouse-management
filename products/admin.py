
from django.contrib import admin

from .models import Category, Product, Supplier, Customer

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Supplier)
admin.site.register(Customer)
