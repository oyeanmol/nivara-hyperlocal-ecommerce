from rest_framework import serializers
from .models import Inventory
from products.serializers import ProductSerializer
from stores.serializers import StoreSerializer

class InventorySerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    store = StoreSerializer(read_only=True)
    final_price = serializers.SerializerMethodField()

    class Meta:
        model = Inventory
        fields = [
            'id',
            'product',
            'store',
            'price',
            'discount_price',
            'final_price',
            'last_updated',
            'stock',
            
        ]

    def get_final_price(self, obj):
        return obj.get_final_price()

class InventoryWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = ['store', 'product', 'stock', 'price', 'discount_price']