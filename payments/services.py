
from .models import Payment
from decimal import Decimal





class PaymentService:
    @staticmethod
    def create_payment_session(borrowing, amount):
        
        payment = Payment.objects.create(
            borrowing=borrowing,
            money_to_pay=amount,
            session_id="test-session-123",
            session_url="https://example.com/session",
            status="PENDING",
            type="PAYMENT",
        )
        return payment


