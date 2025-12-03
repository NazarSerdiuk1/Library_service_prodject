from rest_framework import serializers
from borrowings.models import Borrowing
from books.serializers import BookSerializer
from users.serializers import UserSerializer
from books.models import Book


class BorrowingSerializer(serializers.ModelSerializer):
    book = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all())
    book_info = BookSerializer(source="book", read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Borrowing
        fields = [
            "id",
            "borrow_date",
            "expected_return_date",
            "actual_return_date",
            "book",
            "book_info",
            "user",
        ]
        read_only_fields = ["borrow_date", "actual_return_date", "user"]
