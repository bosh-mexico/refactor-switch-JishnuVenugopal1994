from payment_processor import PaymentProcessor

class GooglePayProcessor(PaymentProcessor):
    def process(self, amount: float):
        return f"Processing GooglePay payment of ${amount:.2f}"