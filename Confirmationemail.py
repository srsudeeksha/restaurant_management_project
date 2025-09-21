from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
import logging

logger = logging.getLogger(__name__)

def send_order_confirmation_email(order_id, customer_email, order_details):
    """
    Sends an order confirmatiion email to the customer.

    Args:
        order_id (str or int):The ID of the order.
        customer_email(str): The customer's email address.
        order_details(str): Summary/details of the order.

    Returns:
        (bool,str):Tuple containing  success status and message.
    """
    subject = f"order confirmatiion-Order #{order_id}"
    message = (
        f"Thank You for your order!\n\n"
        f"Order ID:{Order_id}\n"
        f"Order Details:\n{order_details}\n\n"
        "We appreciate your business."
    )
    from_email = settings.DEFAULT_FROM_EMAIL

    try:
        send_mail(
            subject=subject,
            message = message,
            from_email=from_email,
            recipient_list = [customer_email],
            fail_silently=False,
        )
        return True, "Order Confirmation email sent successfully."
    except BadHeaderError:
        logger.error("Invalid header found when sending order confirmation for order %s", order_id)
        return False, "Invalid email header."
    except Exception as e:
        logger.exception("Failed to send order confirmation for order %s:%s", order_id, str(e))
        return False, f"Email sending failed:{str(e)}"