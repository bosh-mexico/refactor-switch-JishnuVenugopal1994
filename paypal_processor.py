from payment_processor import PaymentProcessor

class PayPalProcessor(PaymentProcessor):
    def process(self, amount: float):
        return f"Processing PayPal payment of ${amount:.2f}"