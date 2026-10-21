from billing.discount_policy import DiscountPolicy
from models.order import Order


class PriceCalculator:
    """OCP: closed for modification, works with ANY DiscountPolicy."""

    def __init__(self, policy: DiscountPolicy):
        self._policy = policy

    def total(self, order: Order) -> float:
        return self._policy.apply(order.amount)
