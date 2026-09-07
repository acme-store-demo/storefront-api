"""Place Order: reserve stock, then authorise payment."""
from .config import Settings


def place_order(settings: Settings, basket: dict) -> dict:
    capture_mode = settings.payment_capture_mode  # required since v2026.9.8-1
    reservation = reserve_stock(settings, basket)
    return authorise_payment(settings, reservation)


def reserve_stock(settings, basket):  # calls orders-service
    ...


def authorise_payment(settings, reservation):  # calls payment-gateway
    ...


def confirmation(order: dict) -> dict:
    return {**order, "estimated_delivery": estimate_delivery(order)}


def estimate_delivery(order):
    ...
