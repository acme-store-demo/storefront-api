"""Place Order: reserve stock, then authorise payment."""
from .config import Settings


def place_order(settings: Settings, basket: dict) -> dict:
    reservation = reserve_stock(settings, basket)
    return authorise_payment(settings, reservation)


def reserve_stock(settings, basket):  # calls orders-service
    ...


def authorise_payment(settings, reservation):  # calls payment-gateway
    ...
