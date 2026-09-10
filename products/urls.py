from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CategoryViewSet, ProductViewSet, SupplierViewSet, CustomerViewSet


router = DefaultRouter()
router.register('categories', CategoryViewSet, basename='category')
router.register('products', ProductViewSet, basename='product')
router.register('suppliers', SupplierViewSet, basename='supplier')
router.register('customers', CustomerViewSet, basename='customer')

urlpatterns = [
    path('', include(router.urls)),
]
