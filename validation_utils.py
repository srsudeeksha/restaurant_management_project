from django.core.validators import validate_email
from django.core.exceptions import ValidationError

def is_valid_email(email):
    """
    validate an email using django's built-in validator.
    Args:
        email(str): The email address to validate.

    Returns:
        bool: True if valid, False otherwise.
    """
    try:
        validate_email(email)
        return True
    except ValidationError:
        return False
    