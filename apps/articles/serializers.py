from rest_framework import serializers

from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"

class ArticleCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = (
            "image",
            "title",
            "content",
            "public",
            "user",
        )
        read_only_fields = ("user",)

class ArticleUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = (
            "image",
            "title",
            "content",
            "public"
        )