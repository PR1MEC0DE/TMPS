from billing.price_calculator import PriceCalculator
from models.order import Order
from notification.notifier import Notifier
from printing.invoice_printer import InvoicePrinter
from storage.interfaces import OrderWriter
from validation.order_validator import OrderValidator


class OrderService:
    """DIP: high-level module; every dependency is an injected abstraction
    (OrderWriter, Notifier) or a small single-purpose collaborator."""

    def __init__(self,
                 validator: OrderValidator,
                 calculator: PriceCalculator,
                 printer: InvoicePrinter,
                 repository: OrderWriter,
                 notifier: Notifier):
        self._validator = validator
        self._calculator = calculator
        self._printer = printer
        self._repository = repository
        self._notifier = notifier

    def place_order(self, order: Order) -> None:
        self._validator.validate(order)
        total = self._calculator.total(order)
        self._repository.save(order, total)
        self._notifier.notify(self._printer.print_invoice(order, total))
