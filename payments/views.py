from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from borrowings.models import Borrowing
from notifications.services import notify_successful_payment
from .serializers import PaymentSerializer
from .services import PaymentService
from .models import Payment


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    @action(detail=False, methods=["post"])
    def create_session(self, request):
        """
        Создаём фиктивный платеж для borrowings.
        """
        borrowing_id = request.data.get("borrowing_id")
        borrowing = Borrowing.objects.get(id=borrowing_id)
        price = 5  # фиксированная сумма

        payment = PaymentService.create_payment_session(
            borrowing=borrowing, amount=price
        )
        return Response(PaymentSerializer(payment).data)

    @action(detail=False, methods=["post"])
    def success(self, request):
        """
        Симуляция успешной оплаты.
        """
        session_id = request.data.get("session_id")
        payment = Payment.objects.get(session_id=session_id)
        payment.status = "PAID"
        payment.save()

        notify_successful_payment(payment)
        return Response({"detail": "Payment successful"})

    @action(detail=False, methods=["post"])
    def cancel(self, request):
        """
        Симуляция отмены оплаты.
        """
        return Response({"detail": "Payment cancelled"})
