
from enum import Enum

# Define Payment Modes
class PaymentMode(Enum):
    PAYPAL = 1
    GOOGLEPAY = 2
    CREDITCARD = 3
    UNKNOWN = 99

# SOLID: PaymentProcessor base class
class PaymentProcessor:
    def process(self, amount: float):
        raise NotImplementedError("Process method must be implemented.")

class PayPalProcessor(PaymentProcessor):
    def process(self, amount: float):
        print(f"Processing PayPal payment of ${amount:.2f}")
        # Placeholder for PayPal API integration

class GooglePayProcessor(PaymentProcessor):
    def process(self, amount: float):
        print(f"Processing GooglePay payment of ${amount:.2f}")
        # Placeholder for GooglePay API integration

class CreditCardProcessor(PaymentProcessor):
    def process(self, amount: float):
        print(f"Processing Credit Card payment of ${amount:.2f}")
        # Placeholder for Credit Card API integration

class UnsupportedPaymentProcessor(PaymentProcessor):
    def process(self, amount: float):
        print("Invalid payment mode selected!")

# Factory for processor selection
def get_payment_processor(mode: PaymentMode) -> PaymentProcessor:
    if mode == PaymentMode.PAYPAL:
        return PayPalProcessor()
    elif mode == PaymentMode.GOOGLEPAY:
        return GooglePayProcessor()
    elif mode == PaymentMode.CREDITCARD:
        return CreditCardProcessor()
    else:
        return UnsupportedPaymentProcessor()

# Checkout function
def checkout(mode: PaymentMode, amount: float):
    processor = get_payment_processor(mode)
    processor.process(amount)

# Example usage
if __name__ == "__main__":
    amount = 150.75
    checkout(PaymentMode.PAYPAL, amount)
    checkout(PaymentMode.GOOGLEPAY, amount)
    checkout(PaymentMode.CREDITCARD, amount)
    checkout(PaymentMode.UNKNOWN, amount)