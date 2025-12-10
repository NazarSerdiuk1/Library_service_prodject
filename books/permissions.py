from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrReadOnly(BasePermission):
    """
    Allows only the administrator to change data (POST, PUT, PATCH, DELETE),
    others can only read (GET, HEAD, OPTIONS).
    """

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True

        return request.user and request.user.is_staff
