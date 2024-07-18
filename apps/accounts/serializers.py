from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import User

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField()

    class Meta:
        model = User
        fields = (
            "email",
            "password",
            "role",
        )

    def validate_password(self, value: str) -> str:
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
