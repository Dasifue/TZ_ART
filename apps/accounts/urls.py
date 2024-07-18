from django.urls import path

from .views import UserCreationAPIView, SubscribeToAuthorAPIView

urlpatterns = [
    path("register/", UserCreationAPIView.as_view()),
    path("subscribe/", SubscribeToAuthorAPIView.as_view())
]
