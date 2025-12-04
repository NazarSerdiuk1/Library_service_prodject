import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from borrowings.models import Borrowing
from books.models import Book
from django.contrib.auth import get_user_model

User = get_user_model()


@pytest.mark.django_db
def test_create_borrowing_decreases_inventory():
    user = User.objects.create_user(
        email="test@example.com", password="pass1234", username="testuser"
    )

    book = Book.objects.create(title="Book 1", inventory=2)

    client = APIClient()
    client.force_authenticate(user)

    data = {"book": book.id, "expected_return_date": "2025-01-01"}

    url = reverse("borrowing-list")
    response = client.post(url, data, format="json")

    book.refresh_from_db()

    assert response.status_code == 201
    assert Borrowing.objects.count() == 1
    assert book.inventory == 1  # decreased by 1


@pytest.mark.django_db
def test_return_book_increases_inventory():
    user = User.objects.create_user(
        email="test@example.com", password="pass1234", username="testuser"
    )

    book = Book.objects.create(title="Book 1", inventory=1)

    borrowing = Borrowing.objects.create(
        user=user,
        book=book,
        expected_return_date="2025-01-01",
    )

    client = APIClient()
    client.force_authenticate(user)

    url = reverse("borrowing-return-book", args=[borrowing.id])
    response = client.post(url)

    book.refresh_from_db()
    borrowing.refresh_from_db()

    assert response.status_code == 200
    assert borrowing.actual_return_date is not None
    assert book.inventory == 2  # increased by 1
