"Articles models"

from django.db import models

from apps.accounts.models import User

class Article(models.Model):
    "Article model"
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="articles")
    image = models.ImageField("Image", upload_to="articles", null=True, blank=True)
    title = models.CharField("Title", max_length=100)
    content = models.TextField("Content", null=True, blank=True)
    public = models.BooleanField("Is public", default=True)
    creation_date = models.DateTimeField("Creation date", auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.title}"
