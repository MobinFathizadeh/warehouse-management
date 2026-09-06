from django.urls import path, include
from rest_framework import routers
from rest_framework.routers import DefaultRouter

from .views import WarehouseViewSet, LocationViewSet



router = DefaultRouter()
router.register(r'warehouses', WarehouseViewSet, basename='warehouses')


urlpatterns = [
    path('',include(router.urls)),
    path('warehouses/<int:warehouse_id>/locations/', LocationViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('warehouses/<int:warehouse_id>/locations/<int:pk>/', LocationViewSet.as_view({'get': 'retrieve', 'patch': 'partial_update'})),
]