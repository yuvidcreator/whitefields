import os
import sys

from paypalcheckoutsdk.core import PayPalHttpClient, SandboxEnvironment


class PayPalClient:
    def __init__(self):
        # self.client_id = "AW4i0YtVvlnmtQEyngdcTuqh7DDyQII7PqOO_ztcySL74h66OdnSWMukY0CK20J5Yd6M6SQIXCiwpBbg"
        # self.client_secret = "EL5G2oTeKVje5HsCjKC02Dm7Spu6CXmP7wLgN8moA_hUNz1EZKm9iFtJ8nNRU9AHUyAlQ03mWfKjwQ_j"
        self.client_id = os.environ.get("PAYPAL_CLIENT_ID")
        self.client_id = os.environ.get("PAYPAL_SECRETE_KEY")
        self.environment = SandboxEnvironment(client_id=self.client_id, client_secret=self.client_secret)
        self.client = PayPalHttpClient(self.environment)
