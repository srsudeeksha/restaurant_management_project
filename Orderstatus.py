from django.db import models

class OrderStatus(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    order_date=models.DateTimeField(auto_now_add=True)

    status = models.ForeignKey(
        OrderStatus,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="orders"
    )

    def __str__(self):
        return f"Order #{self.id}-{self.customer_name}"