"Articles permissions"

from rest_framework import permissions

from .models import User

class IsAuthor(permissions.BasePermission):
    "Permission class checks is user author"

    def has_permission(self, request, view) -> bool:
        "method checks is user role is AUTHOR"
        return request.user.role == User.AUTHOR

    def has_object_permission(self, request, view, obj) -> bool:
        "method checks is user article's author"
        return obj.user.id == request.user.id
