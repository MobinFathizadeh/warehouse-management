from django.shortcuts import render
from rest_framework import viewsets, mixins
from rest_framework.response import Response

from .models import Warehouse, Location
from .serializers import WarehouseSerializer, LocationSerializer, LocationTreeSerializer



class WarehouseViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet
):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer



class LocationViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet
):
    serializer_class = LocationSerializer

    def get_queryset(self):
        return Location.objects.filter(warehouse_id=self.kwargs['warehouse_id'])

    def list(self, request, *args, **kwargs):
        roots = self.get_queryset().filter(parent=None)
        serializer = LocationTreeSerializer(roots, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(warehouse_id=self.kwargs['warehouse_id'])