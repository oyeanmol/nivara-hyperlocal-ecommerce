from django.db import models
from stores.models import Store
from products.models import Product


class Inventory(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='inventories')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='inventories')
    stock = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['store', 'product'], name='unique_store_product')
        ]

    def get_final_price(self):
        return self.discount_price if self.discount_price is not None else self.price

    def __str__(self):
        return f"{self.product.name} - {self.store.name} - ₹{self.get_final_price()}"