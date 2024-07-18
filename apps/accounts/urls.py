from django.urls import path

from .views import UserCreationAPIView

urlpatterns = [
    path("register/", UserCreationAPIView.as_view())
]
