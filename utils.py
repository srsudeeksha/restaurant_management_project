import string 
import secrets
from .models import Order

def generate_unique_order_id(length=8):
    chars = string.ascii_uppercase + string.digits
    while True:
        candidate = ''.join(secrets.choice(chars)for _ in range(length))
        if not Order.objects.filter(order_id=candidate).exists():
            return candidate