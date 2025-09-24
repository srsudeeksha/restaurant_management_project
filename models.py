from django.db import models

class OrderManager(models.Manager):
    def by_status(self, status):
        return self.filter(status=status)

class Order(models.Model):
    STATUS_CHOICES=[
        ('pending','Pending'),
        ('completed','Completed'),
        ('cancelled', 'Cancelled'),
    ]

    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    objects = OrderManager()