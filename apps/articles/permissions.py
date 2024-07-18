from rest_framework import permissions

from .models import User

class IsAuthor(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.role == User.AUTHOR

    def has_object_permission(self, request, view, obj):
        return obj.user.id == request.user.id
