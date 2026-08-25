from django.shortcuts import render
from rest_framework import viewsets, mixins

from .models import Warehouse
from .serializers import WarehouseSerializer



class WarehouseViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet
):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer
