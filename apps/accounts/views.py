"Accounts views"

from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from .models import User, Subscribe
from .serializers import UserRegistrationSerializer, SubscribeSerializer
from .permissions import IsSubscriber

class UserCreationAPIView(CreateAPIView):
    "API View for user creation"

    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]


class SubscribeToAuthorAPIView(CreateAPIView):
    "API View for subscribe creation"

    queryset = Subscribe.objects.all()
    serializer_class = SubscribeSerializer
    permission_classes = [IsAuthenticated, IsSubscriber]

    def perform_create(self, serializer: SubscribeSerializer) -> None:
        "method provides subscriber for serializer class"
        serializer.save(subscriber_id=self.request.user.id)
