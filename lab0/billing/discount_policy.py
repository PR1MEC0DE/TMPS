from abc import ABC, abstractmethod


class DiscountPolicy(ABC):
    """OCP: abstraction that new discounts extend."""

    @abstractmethod
    def apply(self, amount: float) -> float:
        """Return the amount after the discount."""
