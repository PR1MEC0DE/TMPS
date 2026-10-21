from abc import ABC, abstractmethod


class Notifier(ABC):
    """DIP: abstraction that OrderService depends on."""

    @abstractmethod
    def notify(self, message: str) -> None: ...
