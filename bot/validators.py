def validate_order(order_type, price):
    if order_type.upper() == "LIMIT" and price is None:
        raise ValueError(
            "Price is required for LIMIT orders."
        )