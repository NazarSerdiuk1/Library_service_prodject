from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from books import serializers
from .models import Borrowing
from .serializers import BorrowingSerializer
from books.models import Book
from django.utils.timezone import now


class BorrowingViewSet(viewsets.ModelViewSet):
    queryset = Borrowing.objects.all()
    serializer_class = BorrowingSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        book = serializer.validated_data["book"]
        if book.inventory < 1:
            raise serializers.ValidationError("Book not available.")
        book.inventory -= 1
        book.save()
        serializer.save(user=self.request.user)

    @action(detail=True, methods=["post"])
    def return_book(self, request, pk=None):
        borrowing = self.get_object()
        if borrowing.actual_return_date:
            return Response({"detail": "Already returned."}, status=400)
        borrowing.actual_return_date = now().date()
        borrowing.book.inventory += 1
        borrowing.book.save()
        borrowing.save()
        return Response({"detail": "Book returned."})
