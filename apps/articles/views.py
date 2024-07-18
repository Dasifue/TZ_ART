"Articles views"

from django.db.models import QuerySet
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from apps.accounts.permissions import IsSubscriber

from .models import Article
from .serializers import (
    ArticleSerializer,
    ArticleCreationSerializer,
    ArticleUpdateSerializer,
)
from .permissions import IsAuthor

class PublicArticlesListAPIView(ListAPIView):
    "List of public articles"
    queryset = Article.objects.filter(public=True)
    serializer_class = ArticleSerializer

class ArticleCreateAPIView(CreateAPIView):
    "API View for article creation"
    queryset = Article.objects.all()
    serializer_class = ArticleCreationSerializer
    permission_classes = [IsAuthenticated, IsAuthor]

    def perform_create(self, serializer: ArticleCreationSerializer) -> None:
        "method provides user for serializer class"
        serializer.save(user_id=self.request.user.id)

class ArticleUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    "API View for update and delete article"
    serializer_class = ArticleUpdateSerializer
    permission_classes = [IsAuthenticated, IsAuthor]

    def get_queryset(self) -> QuerySet[Article]:
        "method returns QuerySet of user's owning articles"
        return Article.objects.filter(user_id=self.request.user.id)

class PrivateArticlesAPIView(ListAPIView):
    "List of private articles"
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated, IsSubscriber]

    def get_queryset(self) -> QuerySet[Article]:
        "method returns QuerySet of private articles"
        subscribes = self.request.user.subscribes.values_list("author__id", flat=True)
        return Article.objects.filter(user__id__in=subscribes, public=False)
