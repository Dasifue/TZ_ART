from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from .models import Article
from .serializers import (
    ArticleSerializer,
    ArticleCreationSerializer,
    ArticleUpdateSerializer,
)
from apps.accounts.permissions import IsSubscriber
from .permissions import IsAuthor

class PublicArticlesListAPIView(ListAPIView):

    queryset = Article.objects.filter(public=True)
    serializer_class = ArticleSerializer

class ArticleCreateAPIView(CreateAPIView):

    queryset = Article.objects.all()
    serializer_class = ArticleCreationSerializer
    permission_classes = [IsAuthenticated, IsAuthor]

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user.id)

class ArticleUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):

    serializer_class = ArticleUpdateSerializer
    permission_classes = [IsAuthenticated, IsAuthor]

    def get_queryset(self):
        return Article.objects.filter(user_id=self.request.user.id)

class PrivateArticlesAPIView(ListAPIView):

    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated, IsSubscriber]

    def get_queryset(self):
        subscribes = self.request.user.subscribes.values_list("author__id", flat=True)
        return Article.objects.filter(user__id__in=subscribes, public=False)
