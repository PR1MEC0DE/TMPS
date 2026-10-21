from storage.interfaces import OrderReader


class ReadOnlyArchive(OrderReader):
    """ISP: not forced to implement save(), which it would never use."""

    def __init__(self, data: list):
        self._data = data

    def all_orders(self) -> list:
        return list(self._data)
