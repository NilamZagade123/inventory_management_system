
from rest_framework import serializers
from . models import Supplier,Inventory

#Model serializer for read particuler Supplier fields
class SupplierSerializer(serializers.ModelSerializer):
    # specify model and fields
    class Meta:
        model = Supplier
        fields = ['name']


#Model serializer for read particuler inventory fields
class InventoryReadSerializer(serializers.ModelSerializer):
    # specify model and fields
    class Meta:
        model = Inventory
        fields = ['id','name','availability','supplier']

    supplier = SupplierSerializer()



#Model serializer for read all inventory fields
class InventoryDataReadSerializer(serializers.ModelSerializer):
    # specify model and fields
    class Meta:
        model = Inventory
        fields = ['id','name','description','note','stock','availability','supplier']

    supplier = SupplierSerializer()
