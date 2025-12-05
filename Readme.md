Library API

REST API for managing books, users, and loans.
Supports user registration, profile retrieval and updating, book management (for administrators only), as well as a system for borrowing and returning books.
The project includes Swagger documentation and tests.

Project structure
library_service_prodject/
│
├── books/
    ├──tests
        ├──test_books_api.py
    ├──admin.py
    ├──models.py
    ├──serializers.py
    ├──urls.py
    ├──views.py
├── borrowings/
    ├──tests
        ├──test_borrowings_api.py
    ├──admin.py
    ├──models.py
    ├──serializers.py
    ├──urls.py
    ├──views.py
│
├── library_service_prodject/
│   ├── settings.py
│   ├── urls.py
├── users/
    ├──tests
        ├──test_users_api.py
    ├──admin.py
    ├──models.py
    ├──serializers.py
    ├──urls.py
    ├──views.py
├──pytest.ini
├── manage.py
├── README.md
├──requirements.txt

Project description
Functionality:
-User registration
-Viewing and updating profiles
-Book management (CRUD) — for administrators only
-Book borrowing (inventory reduction)
-Book returns (inventory increase)
-Automatic generation of Swagger documentation
-Test coverage pytest + coverage

Technologies:
-Python 3.10+
-Django 5
-Django REST Framework
-drf-spectacular (Swagger)
-pytest, pytest-django
-coverage
-SQLite/PostgreSQL


Installation and launch:
git clone https://github.com/NazarSerdiuk1/Library_service_prodject.git
cd library_service_prodject
Virtual environment
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate  # Linux/Mac
Installing dependencies
pip install -r requirements.txt
Application of migrations
python manage.py migrate
Creating a superuser
python manage.py createsuperuser
Starting the server
python manage.py runserver

API endpoints
Users
Registration: POST /api/users/register/
Obtaining/updating a profile:
GET /api/users/<id>/
PUT /api/users/<id>/
Books
List of books: GET /api/books/
Creating a book (admin): POST /api/books/
Details:GET /api/books/<id>/
Borrowings
Create a borrowing: POST /api/borrowings/
Return the book: POST /api/borrowings/<id>/return_book/

Swagger documentation
Swagger UI: http://127.0.0.1:8000/api/schema/swagger/

Settings in settings.py
REST_FRAMEWORK = {
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}

SPECTACULAR_SETTINGS = {
    "TITLE": "Library API",
    "DESCRIPTION": "API для управления книгами и заимствованиями.",
    "VERSION": "1.0.0",
}
Connection in urls.py:
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView
)

urlpatterns = [
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/schema/swagger/", SpectacularSwaggerView.as_view(url_name="schema")),
    path("api/schema/redoc/", SpectacularRedocView.as_view(url_name="schema")),
]

Tests:
python -m pytest
