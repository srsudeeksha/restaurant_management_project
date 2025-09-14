from django.db import models

class OrderStatus(models.Model):
    name = models.CharField(max_length=50, unique=True)

    PENDING = 'Pending'
    PROCESSING = 'Processing'
    COMPLETED = 'Completed'
    CANCELLED = 'Cancelled'

def __str__(self):
    return self.name