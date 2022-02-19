from rest_framework import serializers

from inventory.models import Supplier, Inventory

class SupplierSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Supplier
        fields = ('name',)

class InventorySerializer(serializers.HyperlinkedModelSerializer):

    supplier = SupplierSerializer()

    class Meta:
        model = Inventory
        fields = ('id','name','description','note','stock','availability','supplier')

