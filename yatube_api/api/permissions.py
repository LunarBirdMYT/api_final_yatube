from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """Пермишн разрешающий автору всё, безопасные методы остальным."""

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user
