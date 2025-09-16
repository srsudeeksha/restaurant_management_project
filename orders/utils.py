import string
import secrets

def generate_coupon_code(length=10, exists_func=None):
    """
    Generate a uniques alphanumeric coupon code.
    Length: Length of the generate code.
    exists_func: Callable that checks code uniqueness(return True if code ex If None, uniqueness is not enforced.)
    """
    chars = string.ascii_uppercase + string.digits
    while True:
        code=''.join(secrets.choice(chars)for _ in range(length))
        if exists_func:
            if not exists_func(code):
                return code
        else:
            return code