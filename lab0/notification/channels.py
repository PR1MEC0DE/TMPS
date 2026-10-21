from notification.notifier import Notifier


class EmailNotifier(Notifier):
    def notify(self, message: str) -> None:
        print(f"[EMAIL] {message}")


class SmsNotifier(Notifier):
    def notify(self, message: str) -> None:
        print(f"[SMS] {message}")
