from django.contrib import admin

from .models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "title", "public", "creation_date")
    list_display_links = ("id", "user", "title")
    search_fields = ("id", "user", "title")
    list_filter = ("public",)
