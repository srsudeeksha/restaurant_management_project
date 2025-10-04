import re

def is_valid_email(email):
    """
    Validate an email address using regex.
    Return True if the email format is valid, False Otherwise.
    """
    pattern = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    return bool(re.match(pattern, email))
    