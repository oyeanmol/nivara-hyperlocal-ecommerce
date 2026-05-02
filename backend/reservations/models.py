from django.db import models
from django.core.validators import MinValueValidator
from users.models import User
from inventory.models import Inventory


class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reservations')
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE, related_name='reservations')
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} reserved {self.quantity} of {self.inventory.product.name} from {self.inventory.store.name}"