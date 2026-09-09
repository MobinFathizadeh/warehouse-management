from rest_framework import serializers

from .models import Warehouse, Location


class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = ['id', 'code', 'name', 'address', 'status']





class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'warehouse', 'parent', 'code', 'name', 'type']
        extra_kwargs = {'warehouse': {'read_only': True},}


class LocationTreeSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()

    class Meta:
        model = Location
        fields = ['id', 'code', 'name', 'type', 'children']

    def get_children(self, obj):
        children = obj.children.all()
        return LocationTreeSerializer(children, many=True).data