from rest_framework import viewsets
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils.timezone import now
from notifications.services import notify_new_borrowing, notify_return
from .models import Borrowing
from .serializers import BorrowingSerializer


class BorrowingViewSet(viewsets.ModelViewSet):
    """
    CRUD for book borrowing.
    - create: Creates a new loan (decreases the book's inventory by 1)
    - list: Gets a list of loans
    - retrieve: Gets loan details
    - update/partial_update: Updates a loan
    - destroy: Deletes a loan
    """

    queryset = Borrowing.objects.all()
    serializer_class = BorrowingSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        book = serializer.validated_data["book"]
        if book.inventory < 1:
            raise serializers.ValidationError("Book not available.")
        book.inventory -= 1
        book.save()

        borrowing = serializer.save(user=self.request.user)

        notify_new_borrowing(borrowing)

    @action(detail=True, methods=["post"])
    def return_book(self, request, pk=None):
        """
        Book returned by user.
        - Sets actual_return_date = today
        - Increases book inventory by 1
        - Returns a message about the result
        """
        borrowing = self.get_object()
        if borrowing.actual_return_date:
            return Response({"detail": "Already returned."}, status=400)
        borrowing.actual_return_date = now().date()
        borrowing.book.inventory += 1
        borrowing.book.save()
        borrowing.save()

        notify_return(borrowing)
        
        return Response({"detail": "Book returned."})
