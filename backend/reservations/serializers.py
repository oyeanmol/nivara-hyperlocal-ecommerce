from rest_framework import serializers
from .models import Reservation

class ReservationSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='inventory.product.name', read_only=True)
    store_name = serializers.CharField(source='inventory.store.name', read_only=True)

    class Meta:
        model = Reservation
        fields = [
            'id',
            'user',
            'inventory',
            'product_name',
            'store_name',
            'quantity',
            'created_at'
        ]