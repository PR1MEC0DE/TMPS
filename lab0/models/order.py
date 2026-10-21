from dataclasses import dataclass


@dataclass
class Order:
    """SRP: only holds order data."""
    customer: str
    amount: float
    customer_type: str = "regular"
