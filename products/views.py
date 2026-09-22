from django.shortcuts import render
from rest_framework import viewsets, mixins
from rest_framework.response import Response
from django.db import models


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
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.all()

        barcode = self.request.query_params.get('barcode')
        if barcode:
            queryset = queryset.filter(barcode=barcode)

        sku = self.request.query_params.get('sku')
        if sku:
            queryset = queryset.filter(sku=sku)


        category = self.request.query_params.get('category')
        if category:
            queryset = queryset.filter(category_id=category)

        status = self.request.query_params.get('status')
        if status:
            queryset = queryset.filter(status=status)

        search = self.request.query_params.get('search')
        if search:
            queryset = queryset.filter(
                models.Q(name__icontains=search) |
                models.Q(sku__icontains=search) |
                models.Q(barcode__icontains=search)
            )

        return queryset


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