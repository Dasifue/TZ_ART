"User Permissions"

from rest_framework import permissions

from .models import User

class IsSubscriber(permissions.BasePermission):
    "Permission class checks is user subscriber"

    def has_permission(self, request, view) -> bool:
        return request.user.role == User.SUBSCRIBER
