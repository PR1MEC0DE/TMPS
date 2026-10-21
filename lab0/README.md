# SOLID Principles

## Boltunov Igor
* * *

## Objectives:

- Get familiar with the SOLID principles;
- Choose a specific domain (order processing);
- Implement at least 3 SOLID principles in a simple project;

## Used Principles:

- S - Single Responsibility Principle
- O - Open/Closed Principle
- I - Interface Segregation Principle
- D - Dependency Inversion Principle

## Project structure

```
main.py                         # composition root
models/order.py                 # Order (data only)
validation/order_validator.py   # OrderValidator
printing/invoice_printer.py     # InvoicePrinter
billing/discount_policy.py      # DiscountPolicy (abstraction)
billing/discounts.py            # NoDiscount, VipDiscount, BlackFridayDiscount
billing/price_calculator.py     # PriceCalculator
storage/interfaces.py           # OrderWriter, OrderReader
storage/in_memory_repository.py # InMemoryOrderRepository
storage/read_only_archive.py    # ReadOnlyArchive
notification/notifier.py        # Notifier (abstraction)
notification/channels.py        # EmailNotifier, SmsNotifier
services/order_service.py       # OrderService
services/report_service.py      # ReportService
```

Run with: `python main.py`

## Implementation

### S - Single Responsibility
`Order` only stores data, `OrderValidator` only validates, and `InvoicePrinter`
only formats text. Each class lives in its own file and has one reason to change.

```python
class OrderValidator:
    def validate(self, order: Order) -> None:
        if order.amount <= 0:
            raise ValueError("Order amount must be positive")
```

### O - Open/Closed
`PriceCalculator` depends on the `DiscountPolicy` abstraction. A new discount
(`BlackFridayDiscount`) was added as a new class without editing the calculator.

```python
class BlackFridayDiscount(DiscountPolicy):
    def apply(self, amount: float) -> float:
        return amount * 0.50
```

### I - Interface Segregation
Instead of one large repository interface, there are two small ones:
`OrderWriter` (save) and `OrderReader` (all_orders). `ReadOnlyArchive` implements
only `OrderReader`, and `ReportService` depends only on `OrderReader`.

```python
class ReadOnlyArchive(OrderReader):
    def all_orders(self) -> list:
        return list(self._data)
```

### D - Dependency Inversion
`OrderService` (high-level) depends on `OrderWriter` and `Notifier`
(abstractions), not on concrete classes. Concrete classes are chosen only in
`main.py` and injected through the constructor.

```python
class OrderService:
    def __init__(self, validator, calculator, printer,
                 repository: OrderWriter, notifier: Notifier): ...
```

## Conclusions / Screenshots / Results

```
--- VIP customer, SMS (swapped notifier + policy) ---
[DB] Saved order of Bob
[SMS] Invoice for Bob: amount=100.00, total=80.00
```

Applying SOLID made the code easier to extend (new discounts, notifiers and
storages need only new classes), easier to test (dependencies can be replaced),
and easier to understand (small, focused files).
