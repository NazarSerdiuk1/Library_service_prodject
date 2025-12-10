from enum import Enum


class PaymentStatus(str, Enum):
    PENDING = "PENDING"
    PAID = "PAID"


class PaymentType(str, Enum):
    PAYMENT = "PAYMENT"
    FINE = "FINE"
