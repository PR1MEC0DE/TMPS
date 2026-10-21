from storage.interfaces import OrderReader


class ReportService:
    """ISP: only needs to READ, so it depends on OrderReader only."""

    def __init__(self, reader: OrderReader):
        self._reader = reader

    def summary(self) -> str:
        orders = self._reader.all_orders()
        revenue = sum(total for _, total in orders)
        return f"{len(orders)} orders, revenue={revenue:.2f}"
