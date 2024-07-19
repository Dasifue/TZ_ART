"Articles forms"

from django import forms

from apps.accounts.models import User
from .models import Article

class ArticleCreationForm(forms.ModelForm):
    "article creation form in admin site"

    class Meta:
        "Meta class"
        model = Article
        exclude = ("creation_date",)

    def clean_user(self) -> User:
        "Method checks user's role is AUTHOR"
        user = self.cleaned_data.get("user")
        if user.role != User.AUTHOR:
            self.add_error("user", "user must have role AUTHOR")
        return user
