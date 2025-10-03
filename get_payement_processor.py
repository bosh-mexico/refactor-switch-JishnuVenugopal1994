from payment_mode import PaymentMode
from payment_processor import PaymentProcessor
from paypal_processor import PayPalProcessor
from googlepay_processor import GooglePayProcessor
from creditcard_processor import CreditCardProcessor
from unsupported_payment_processor import UnsupportedPaymentProcessor
from typing import Dict, Type, Optional

# Default processor mapping
DEFAULT_PROCESSORS = {
    PaymentMode.PAYPAL: PayPalProcessor,
    PaymentMode.GOOGLEPAY: GooglePayProcessor,
    PaymentMode.CREDITCARD: CreditCardProcessor,
}

def get_payment_processor(
    mode, 
    processor_map: Optional[Dict[PaymentMode, Type[PaymentProcessor]]] = None
) -> PaymentProcessor:

    # Use provided processor_map or fall back to default
    processors = processor_map if processor_map is not None else DEFAULT_PROCESSORS
    
    if not isinstance(mode, PaymentMode):
        return UnsupportedPaymentProcessor()
        
    processor_cls = processors.get(mode, UnsupportedPaymentProcessor)
    return processor_cls()