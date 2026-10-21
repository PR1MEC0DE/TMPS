from billing.discount_policy import DiscountPolicy


class NoDiscount(DiscountPolicy):
    def apply(self, amount: float) -> float:
        return amount


class VipDiscount(DiscountPolicy):
    def apply(self, amount: float) -> float:
        return amount * 0.80  # 20% off


class BlackFridayDiscount(DiscountPolicy):
    """Added later: no existing file had to be modified (OCP)."""

    def apply(self, amount: float) -> float:
        return amount * 0.50  # 50% off
