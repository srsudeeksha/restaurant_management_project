import logging 
from orders.models import Order

logger = logging.getLogger(__name__)

def update_order_status(order_id, new_status):
    try:
        order = Order.objects.get(id=order_id)
    except Order.DoesNotExist:
        logger.error(f"Order with ID {order_id} does not exist.")
        return False, "Order not found"

    allowed_statuses = [choice[0] for choice in Order.STATUS_CHOICES]
    if new_status not in allowed_statuses:
        logger.error(f"Invalid status '{new_status}'provided for order ID{order_id}.")
        return False, "Invalid status."
    
    old_status = order.status
    order.status=new_status
    order.save()
    logger.info(f"Order ID{order_id} status changed from '{old_status}' to '{new_status}'.")
    return True, "Order status updated."
    