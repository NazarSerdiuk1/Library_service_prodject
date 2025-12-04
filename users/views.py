from rest_framework import generics, permissions
from .serializers import RegisterSerializer, UserSerializer
from django.contrib.auth import get_user_model


User = get_user_model()


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]


class UserProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()
