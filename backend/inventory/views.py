from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Inventory
from .serializers import InventorySerializer

class InventoryView(APIView):
    def get(self, request, product_id):
        inventories = Inventory.objects.filter(product_id=product_id)
        serializer = InventorySerializer(inventories, many=True)
        return Response(serializer.data)