"""Runtime settings, read from deploy/values-*.yaml at start-up."""
import os


class MissingConfigError(RuntimeError):
    """A required setting is absent; there is no default to fall back on."""


class Settings:
    def __init__(self) -> None:
        self.orders_service_url = os.environ["ORDERS_SERVICE_URL"]
        self.checkout_service_url = os.environ["CHECKOUT_SERVICE_URL"]

    @property
    def payment_capture_mode(self) -> str:
        value = os.environ.get("PAYMENT_CAPTURE_MODE")
        if not value:
            raise MissingConfigError("payment_capture_mode is required but not set")
        return value
