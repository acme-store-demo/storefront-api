"""Runtime settings, read from deploy/values-*.yaml at start-up."""
import os

DEFAULT_PAYMENT_CAPTURE_MODE = "authorize_then_capture"


class Settings:
    def __init__(self) -> None:
        self.orders_service_url = os.environ["ORDERS_SERVICE_URL"]
        self.checkout_service_url = os.environ["CHECKOUT_SERVICE_URL"]

    @property
    def payment_capture_mode(self) -> str:
        return os.environ.get("PAYMENT_CAPTURE_MODE", DEFAULT_PAYMENT_CAPTURE_MODE)
