from django.db import models
from customers.models import Customer
from products.models import Product

# Order model

class Order(models.Model):
    LIVE = 1
    DELETE = 0
    DELETE_CHOICES = ((LIVE, 'live'), (DELETE, 'Delete'))
    CART_STAGE, ORDER_CONFIRMED, ORDER_PROCESSED, ORDER_DELIVERD, ORDER_REJECTED = 0, 1, 2, 3, 4
    STATUS_CHOICE = ((ORDER_PROCESSED, 'order_processed'),
                     (ORDER_DELIVERD, 'order_deliverd'),
                     (ORDER_REJECTED, 'order_rejected'))
    order_status = models.IntegerField(choices=STATUS_CHOICE, default=CART_STAGE)
    owner = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, related_name='cart_item')
    delete_status = models.IntegerField(choices=DELETE_CHOICES, default=LIVE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    total_price = models.FloatField(default=0)

    def __str__(self):
        return f"{self.id} {self.owner.user.username} item"

class OrderedItem(models.Model):
    product = models.ForeignKey(Product, related_name='added_carts', on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=1)
    owner = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='added_item')