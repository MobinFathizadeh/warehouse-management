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

    def validate_parent(self, parent):
        if parent is None:
            return parent

        warehouse_id = self.context['view'].kwargs['warehouse_id']
        if parent.warehouse_id != warehouse_id:
            raise serializers.ValidationError('مکان والد باید متعلق به همین انبار باشد')

        if self.instance is not None:
            node = parent
            while node is not None:
                if node.pk == self.instance.pk:
                    raise serializers.ValidationError('مکان نمی‌تواند والد خودش یا زیرمجموعه‌ی خودش باشد')
                node = node.parent

        return parent

    def validate(self, data):
        warehouse_id = self.context['view'].kwargs['warehouse_id']
        code = data.get('code')

        if code is not None:
            duplicates = Location.objects.filter(warehouse_id=warehouse_id, code=code)
            if self.instance is not None:
                duplicates = duplicates.exclude(pk=self.instance.pk)
            if duplicates.exists():
                raise serializers.ValidationError({'code': ['این کد در این انبار قبلاً استفاده شده است']})

        return data


class LocationTreeSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()

    class Meta:
        model = Location
        fields = ['id', 'code', 'name', 'type', 'children']

    def get_children(self, obj):
        children = obj.children.all()
        return LocationTreeSerializer(children, many=True).data