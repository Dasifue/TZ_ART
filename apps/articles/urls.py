from django.urls import path

from .views import (
    PublicArticlesListAPIView,
    ArticleCreateAPIView,
    ArticleUpdateDeleteAPIView,
)

urlpatterns = [
    path('articles/<int:pk>', ArticleUpdateDeleteAPIView.as_view()),
    path('articles/public/', PublicArticlesListAPIView.as_view()),
    path('articles/create/', ArticleCreateAPIView.as_view()),
]
