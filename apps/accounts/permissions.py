from rest_framework import permissions

from .models import User

class IsSubscriber(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.role == User.SUBSCRIBER
