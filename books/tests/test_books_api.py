import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from books.models import Book
from django.contrib.auth import get_user_model

User = get_user_model()


@pytest.mark.django_db
def test_get_books_list():
    Book.objects.create(title="Book 1", inventory=5)
    Book.objects.create(title="Book 2", inventory=1)

    client = APIClient()
    url = reverse("book-list")

    response = client.get(url)

    assert response.status_code == 200
    assert len(response.data) == 2


@pytest.mark.django_db
def test_admin_can_create_book():
    admin = User.objects.create_superuser(
        email="admin@example.com", password="adminpass", username="admin"
    )

    client = APIClient()
    client.force_authenticate(admin)

    data = {"title": "New Book","author": "Griroyi Pims","inventory": 3}

    url = reverse("book-list")
    response = client.post(url, data, format="json")

    assert response.status_code == 201
    assert Book.objects.count() == 1
