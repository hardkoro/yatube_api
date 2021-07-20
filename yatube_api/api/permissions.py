from rest_framework import permissions


class OwnerOrReadOnly(permissions.BasePermission):
    """Разрешение на редактирование объектов только их создателям."""

    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user
