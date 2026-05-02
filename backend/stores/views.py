from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Store
from .serializers import StoreSerializer

class StoreListView(APIView):
    def get(self, request):
        stores = Store.objects.all()
        serializer = StoreSerializer(stores, many=True)
        return Response(serializer.data)