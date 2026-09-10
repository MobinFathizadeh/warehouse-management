from django.shortcuts import render
from rest_framework import viewsets, mixins
from rest_framework.response import Response

from .models import Category, Product, Supplier, Customer
from .serializers import CategorySerializer, CategoryTreeSerializer, ProductSerializer, SupplierSerializer, CustomerSerializer


class CategoryViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet
):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def list(self, request, *args, **kwargs):
        roots = self.get_queryset().filter(parent=None)
        serializer = CategoryTreeSerializer(roots, many=True)
        return Response(serializer.data)



class ProductViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class SupplierViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet
):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


class CustomerViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet
):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer