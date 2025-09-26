from payment_mode import PaymentMode
from payment_processor import PaymentProcessor
from paypal_processor import PayPalProcessor
from googlepay_processor import GooglePayProcessor
from creditcard_processor import CreditCardProcessor
from unsupported_payment_processor import UnsupportedPaymentProcessor

def get_payment_processor(mode) -> PaymentProcessor:

    processor_map = {
        PaymentMode.PAYPAL: PayPalProcessor,
        PaymentMode.GOOGLEPAY: GooglePayProcessor,
        PaymentMode.CREDITCARD: CreditCardProcessor,
    }
    
    if not isinstance(mode, PaymentMode):
        return UnsupportedPaymentProcessor()
        
    processor_cls = processor_map.get(mode, UnsupportedPaymentProcessor)
    return processor_cls()