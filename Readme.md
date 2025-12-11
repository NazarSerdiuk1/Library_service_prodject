# Library API

## Project Description

REST API for managing books, users, and loans.
Supports user registration, profile retrieval and updating, book management (for administrators only), as well as a system for borrowing and returning books.
The project includes Swagger documentation and tests.

## Functionality:
-User registration
-Viewing and updating profiles
-Book management (CRUD) — for administrators only
-Book borrowing (inventory reduction)
-Book returns (inventory increase)
-Automatic generation of Swagger documentation
-Test coverage pytest + coverage
-Send message in Telegram Chat 

## Technologies:
-Python 3.10+
-Django 5
-Django REST Framework
-drf-spectacular (Swagger)
-pytest, pytest-django
-coverage
-PostgreSQL
-Docker
-pytest

## Installation (without Docker)
1. Clone the repository:
    ```bash
    git clone https://github.com/NazarSerdiuk1/Library_service_prodject.git
    ```
2. Navigate to the project folder:
    ```bash
    cd library_service_prodject
    ```
3. Virtual environment:
    ```bash
    python -m venv venv
    venv\Scripts\activate      # Windows
    source venv/bin/activate  # Linux/Mac
    ```
4. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
5. Run migrations:
    ```bash
    python manage.py migrate
    ```
6. Creating a superuser:
    ```bash
    python manage.py createsuperuser
    ```
7. Starting the server:
    ```bash
    python manage.py runserver
    ```
## Running with Docker
1. Build containers:
    ```bash
    docker-compose build
    ```
2. Start services:
   ```bash
   docker-compose up 
   ``` 
3. Run migrations inside the container:
    ```bash
    docker-compose exec web python manage.py migrate
    ```
4. Create a superuser:
    ```bash
    docker-compose exec web python manage.py createsuperuser
    ```
## API endpoints
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

## Swagger documentation
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

## Tests:
    ```bash
    python -m pytest
    ```