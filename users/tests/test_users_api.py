import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model


User = get_user_model()


@pytest.mark.django_db
def test_user_registration():
    client = APIClient()

    data = {
        "email": "test@example.com",
        "password": "strongpass123",
        "first_name": "Test",
        "last_name": "User",
        "username": "testuser",
    }

    url = reverse("register")
    response = client.post(url, data, format="json")

    assert response.status_code == 201
    assert User.objects.count() == 1


@pytest.mark.django_db
def test_get_user_profile():
    user = User.objects.create_user(
        email="test@example.com", password="strongpass123", username="testuser"
    )

    client = APIClient()
    client.force_authenticate(user=user)

    url = reverse("user-profile", args=[user.id])
    response = client.get(url)

    assert response.status_code == 200
    assert response.data["email"] == user.email
