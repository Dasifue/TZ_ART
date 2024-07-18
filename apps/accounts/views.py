from rest_framework.generics import CreateAPIView

from .models import User
from .serializers import UserRegistrationSerializer

class UserCreationAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
