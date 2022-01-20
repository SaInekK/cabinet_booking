from rest_framework import permissions


class IsOwnerAdminOrReadOnly(permissions.BasePermission):
    """Права для владелеца и админа."""

    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or obj.booker == request.user
                or request.user.is_staff or request.user.is_superuser)


class IsAdminOrReadOnly(permissions.BasePermission):
    """Права админа."""

    def has_object_permission(self, request, view):
        return (
                request.method in permissions.SAFE_METHODS
                or request.user.is_staff and request.user.is_superuser
        )


class IsAuthorOrReadOnly(permissions.IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        # if request.method in permissions.SAFE_METHODS:
        #     return True

        return obj.booker == request.user or request.user.is_staff or request.user.is_superuser
