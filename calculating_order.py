def calculate_order_total(order_items):
    """
    Calculate the total price for an order.
    Args:
        order_items (list): A list of dicts, each containing 'quantity' and 'price' keys.

    Return:
        float: The Toral price for the order.
    """
    if not order_items:
        return 0.0
    
    total = 0.0
    for item in order_items:
        quantity = item.get('quantity', 0)
        price = item.get('price',0.0)
        total += quantity * price
    return total 