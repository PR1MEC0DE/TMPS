from models.order import Order


class OrderValidator:
    """SRP: only responsible for validating an order."""

    def validate(self, order: Order) -> None:
        if order.amount <= 0:
            raise ValueError("Order amount must be positive")
        if not order.customer:
            raise ValueError("Customer name is required")
