from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction
from .models import Reservation
from .serializers import ReservationSerializer
from rest_framework.permissions import IsAuthenticated
from inventory.models import Inventory


class ReservationView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        store_id = request.query_params.get('store_id')

        if not store_id:
            reservations = Reservation.objects.filter(user=request.user)
        else:
            reservations = Reservation.objects.filter(
                inventory__store_id=store_id
            )

        serializer = ReservationSerializer(reservations, many=True)
        return Response(serializer.data)

    @transaction.atomic
    def post(self, request):
        user = request.user
        inventory_id = request.data.get('inventory')

        if not inventory_id:
            return Response({"error": "Inventory ID required"}, status=400)

        try:
            quantity = int(request.data.get('quantity'))
        except (TypeError, ValueError):
            return Response({"error": "Invalid quantity"}, status=400)

        try:
            inventory = Inventory.objects.select_for_update().get(id=inventory_id)
        except Inventory.DoesNotExist:
            return Response({"error": "Inventory not found"}, status=404)

        if quantity <= 0:
            return Response({"error": "Invalid quantity"}, status=400)

        if inventory.stock < quantity:
            return Response({"error": "Not enough stock"}, status=400)

        inventory.stock -= quantity
        inventory.save()

        reservation = Reservation.objects.create(
            user=user,
            inventory=inventory,
            quantity=quantity
        )

        serializer = ReservationSerializer(reservation)
        return Response(serializer.data, status=status.HTTP_201_CREATED)