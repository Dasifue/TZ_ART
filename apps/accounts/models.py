from typing import Iterable
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.contrib.auth.hashers import make_password

class CustomUserManager(BaseUserManager):

    def create(self, **kwargs):
        password = kwargs.pop("password", None)
        if password is not None:
            kwargs['password'] = make_password(password)
        return super().create(**kwargs)

    def create_user(self, email, password, **kwargs):
        if not email:
            raise ValueError("User email not specified")

        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **kwargs):
        kwargs.update({
            "is_staff": True,
            "is_active": True,
            "is_superuser": True,
        })
        return self.create_user(email, password, **kwargs)


class User(AbstractUser):
    AUTHOR = 'AUTHOR'
    SUBSCRIBER = 'SUBSCRIBER'
    ROLE_CHOICES = (
        (AUTHOR, 'Author'),
        (SUBSCRIBER, 'Subscriber'),
    )

    email = models.EmailField("Email", unique=True, null=False, blank=False)
    full_name = models.CharField("Full name", max_length=100, null=True, blank=True)
    role = models.CharField("Role", max_length=10, choices=ROLE_CHOICES, default=SUBSCRIBER)

    username = None
    first_name = None
    last_name = None


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return f'{self.email} ({self.role})'


class Subscribe(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="subscribers")
    subscriber = models.ForeignKey(User, on_delete=models.CASCADE, related_name="subscribes")
    creation_date = models.DateTimeField("Subscribe date", auto_now_add=True)

    class Meta:
        unique_together = ['author', 'subscriber']

    def __str__(self) -> str:
        return f'{self.subscriber.email} -> {self.author.email}'
