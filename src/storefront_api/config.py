"""Runtime settings, read from deploy/values-*.yaml at start-up."""
import os


class Settings:
    def __init__(self) -> None:
        self.orders_service_url = os.environ["ORDERS_SERVICE_URL"]
        self.checkout_service_url = os.environ["CHECKOUT_SERVICE_URL"]
