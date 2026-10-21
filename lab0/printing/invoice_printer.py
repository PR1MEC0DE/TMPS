from models.order import Order


class InvoicePrinter:
    """SRP: only responsible for formatting the invoice text."""

    def print_invoice(self, order: Order, total: float) -> str:
        return (f"Invoice for {order.customer}: "
                f"amount={order.amount:.2f}, total={total:.2f}")
