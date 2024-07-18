"Articles serializers"

from rest_framework import serializers

from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    "article reading serializer"

    class Meta:
        "Meta class"
        model = Article
        fields = "__all__"

class ArticleCreationSerializer(serializers.ModelSerializer):
    "article creation serializer"

    class Meta:
        "Meta class"
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
    "article update serializer"

    class Meta:
        "Meta class"
        model = Article
        fields = (
            "image",
            "title",
            "content",
            "public"
        )
