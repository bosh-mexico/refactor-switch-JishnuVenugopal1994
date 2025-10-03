from payment_processor import PaymentProcessor  

class UnsupportedPaymentProcessor(PaymentProcessor):
    def process(self, amount: float):
        return "Invalid payment mode selected!"