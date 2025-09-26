from payment_mode import PaymentMode
from get_payement_processor import get_payment_processor

def checkout(mode, amount: float):
    
    processor = get_payment_processor(mode)
    result = processor.process(amount)
    print(result)