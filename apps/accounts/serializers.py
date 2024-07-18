"Serializers"

from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.db import IntegrityError

from .models import User, Subscribe

class UserRegistrationSerializer(serializers.ModelSerializer):
    "Custom registration serializer"
    password = serializers.CharField()

    class Meta:
        "Meta class"
        model = User
        fields = (
            "email",
            "password",
            "role",
        )

    def validate_password(self, value: str) -> str:
        "method validates password"
        if len(value) < 8:
            raise ValidationError("Password must contain 8 or more chars")

        letter, digit = False, False
        for char in value:
            if char.isalpha():
                letter = True
            elif char.isnumeric():
                digit = True

            if letter and digit:
                break
        else:
            raise ValidationError("Password must contain at least 1 digit and 1 char")
        return value


class SubscribeSerializer(serializers.ModelSerializer):
    "Serializer fom subscribe creation validation"

    class Meta:
        "Meta class"
        model = Subscribe
        fields = (
            "author",
            "subscriber",
        )
        read_only_fields = ("subscriber",)

    def validate_author(self, value: User) -> User:
        "method validates author role"
        if value.role != User.AUTHOR:
            raise ValidationError("The author must have the role AUTHOR")
        return value

    def validate_subscriber(self, value: User) -> User:
        "method validates subscriber role"
        if value.role != User.SUBSCRIBER:
            raise ValidationError("The subscriber must have the role SUBSCRIBER")
        return value

    def save(self, **kwargs) -> Subscribe:
        "Method creates subscribe instance"
        try:
            return super().save(**kwargs)
        except IntegrityError as error:
            raise ValidationError(
                {
                    "detail": "Duplicate key value violates unique constraint"
                }
            ) from error
