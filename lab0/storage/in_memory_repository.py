from models.order import Order
from storage.interfaces import OrderReader, OrderWriter


class InMemoryOrderRepository(OrderWriter, OrderReader):
    """Can read AND write, so it implements both small interfaces."""

    def __init__(self):
        self.orders = []

    def save(self, order: Order, total: float) -> None:
        self.orders.append((order, total))
        print(f"[DB] Saved order of {order.customer}")

    def all_orders(self) -> list:
        return list(self.orders)
