# Thirdparty imports
from rest_framework.permissions import SAFE_METHODS, BasePermission


class AuthorOrNot(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.author


class UserAuth(BasePermission):
    """Даём права на регистрацию."""

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return request.method == 'POST'
        return True

    def has_object_permission(self, request, view, obj):
        if request.method not in SAFE_METHODS:
            return request.user == obj
        return True
