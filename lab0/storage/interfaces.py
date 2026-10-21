from abc import ABC, abstractmethod
from models.order import Order


class OrderWriter(ABC):
    """ISP: small interface for clients that only write."""

    @abstractmethod
    def save(self, order: Order, total: float) -> None: ...


class OrderReader(ABC):
    """ISP: small interface for clients that only read."""

    @abstractmethod
    def all_orders(self) -> list: ...
