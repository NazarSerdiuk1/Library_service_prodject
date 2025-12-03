from django.urls import path
from .views import RegisterView, UserProfileView

urlpatterns = [
    path("users/", RegisterView.as_view(), name="register"),
    path("users/<int:pk>/", UserProfileView.as_view(), name="user-profile"),
]
