import requests
from django.conf import settings
from django.utils.timezone import now
from borrowings.models import Borrowing


def send_telegram_message(text: str):
    """Send a plain text message to Telegram chat."""
    url = f"https://api.telegram.org/bot{settings.TELEGRAM_TOKEN}/sendMessage"

    payload = {
        "chat_id": settings.TELEGRAM_CHAT_ID,  
        "text": text,
        "parse_mode": "HTML",
    }

    try:
        requests.post(url, data=payload)
    except Exception as e:
        print("Telegram error:", e)


def notify_new_borrowing(borrowing: Borrowing):
    text = (
        f"📚 <b>New Borrowing Created</b>\n"
        f"👤 User: {borrowing.user.email}\n"
        f"📖 Book: {borrowing.book.title}\n"
        f"📅 Borrowed: {borrowing.borrow_date}\n"
        f"📆 Expected return: {borrowing.expected_return_date}"
    )
    send_telegram_message(text)


def notify_return(borrowing: Borrowing):
    text = (
        f"🔄 <b>Book Returned</b>\n"
        f"👤 User: {borrowing.user.email}\n"
        f"📖 Book: {borrowing.book.title}\n"
        f"📅 Actual return: {borrowing.actual_return_date}"
    )
    send_telegram_message(text)


def notify_successful_payment(payment):
    text = (
        f"💳 <b>Payment Successful</b>\n"
        f"Borrowing ID: {payment.borrowing.id}\n"
        f"💵 Amount: {payment.money_to_pay}$\n"
        f"Status: {payment.status}"
    )
    send_telegram_message(text)


def check_overdue_borrowings():
    """Call from management command or Celery later."""
    today = now().date()
    overdue = Borrowing.objects.filter(
        actual_return_date__isnull=True,
        expected_return_date__lt=today,
    )

    for bor in overdue:
        send_telegram_message(
            f"⛔ <b>Borrowing Overdue!</b>\n"
            f"User: {bor.user.email}\n"
            f"Book: {bor.book.title}\n"
            f"Expected return: {bor.expected_return_date}\n"
            f"Today: {today}"
        )
