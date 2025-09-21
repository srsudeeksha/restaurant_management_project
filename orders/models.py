from django.db import models
from decimal import Decimal 

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)

class Order(models.Model):

    def calculate_total(self):
        return sum(
            item.menu_item.price * item.quantity
            for item in self.orderitem_set.all()

        )

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    