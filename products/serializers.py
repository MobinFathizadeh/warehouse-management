from rest_framework import serializers
from .models import Category, Product, Supplier, Customer



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'parent', 'name', 'description']


class CategoryTreeSerializer(serializers.ModelSerializer) :
    children = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'children']


    def get_children(self, obj):
        children = obj.children.all()
        return CategoryTreeSerializer(children, many=True).data


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'category', 'sku', 'name', 'barcode', 'description', 'unit', 'status']


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ['id', 'name', 'phone', 'email', 'address', 'status']


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'name', 'phone', 'email', 'address', 'status']