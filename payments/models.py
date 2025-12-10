from django.db import models
from borrowings.models import Borrowing
from library_service_prodject.constants import PaymentStatus, PaymentType


class Payment(models.Model):
    status = models.CharField(
        max_length=10,
        choices=[(s.value, s.value) for s in PaymentStatus],
        default=PaymentStatus.PENDING.value,
    )

    type = models.CharField(
        max_length=10, choices=[(t.value, t.value) for t in PaymentType]
    )
    borrowing = models.ForeignKey(
        Borrowing, on_delete=models.CASCADE, related_name="payments"
    )
    session_url = models.URLField()
    session_id = models.CharField(max_length=255)
    money_to_pay = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"Payment {self.id} ({self.status})"
