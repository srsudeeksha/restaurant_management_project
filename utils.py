from django.core.mail import send_mail
from django.conf import settings
import logging 

def send_email(recipient_email,subject, message):
    try:
        send_email(
            subject,
            message,
            settings.DEFAULT_FORM_EMAIL,
            [recipient_email],
            fail_silently=False,
        )
        return True
    except Exception as e:
        logging.error(f"Email sending failed to{recipient_email}:{e}")
        return False