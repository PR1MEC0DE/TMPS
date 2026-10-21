"""Composition root: the only place where concrete classes are chosen."""
from billing.discounts import BlackFridayDiscount, NoDiscount, VipDiscount
from billing.price_calculator import PriceCalculator
from models.order import Order
from notification.channels import EmailNotifier, SmsNotifier
from printing.invoice_printer import InvoicePrinter
from services.order_service import OrderService
from services.report_service import ReportService
from storage.in_memory_repository import InMemoryOrderRepository
from storage.read_only_archive import ReadOnlyArchive
from validation.order_validator import OrderValidator


def build_service(policy, notifier, repo):
    return OrderService(OrderValidator(), PriceCalculator(policy),
                        InvoicePrinter(), repo, notifier)


if __name__ == "__main__":
    repo = InMemoryOrderRepository()

    print("--- Regular customer, email ---")
    build_service(NoDiscount(), EmailNotifier(), repo).place_order(
        Order("Alice", 100))

    print("\n--- VIP customer, SMS (swapped notifier + policy) ---")
    build_service(VipDiscount(), SmsNotifier(), repo).place_order(
        Order("Bob", 100, "vip"))

    print("\n--- Black Friday (new policy, no old code modified) ---")
    build_service(BlackFridayDiscount(), EmailNotifier(), repo).place_order(
        Order("Carol", 200))

    print("\n--- Reports (ISP: readers only need OrderReader) ---")
    print("Live repo :", ReportService(repo).summary())
    archive = ReadOnlyArchive([(Order("Old", 50), 50.0)])
    print("Archive   :", ReportService(archive).summary())

    print("\n--- Invalid order ---")
    try:
        build_service(NoDiscount(), EmailNotifier(), repo).place_order(
            Order("Dave", -5))
    except ValueError as e:
        print(f"[ERROR] {e}")
