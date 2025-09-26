from payment_mode import PaymentMode
from checkout import checkout

# Example usage
if __name__ == "__main__":
    amount = 150.75
    checkout(PaymentMode.PAYPAL, amount)
    checkout(PaymentMode.GOOGLEPAY, amount)
    checkout(PaymentMode.CREDITCARD, amount)
    checkout(99, amount)