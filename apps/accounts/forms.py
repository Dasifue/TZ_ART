from django import forms
from django.core.exceptions import ValidationError

from .models import User, Subscribe


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'email',
            'role'
        ]

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            self.add_error("password1", "Passwords didn't match")
            self.add_error("password2", "Passwords didn't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class SubscribeCreationForm(forms.ModelForm):
    class Meta:
        model = Subscribe
        fields = "__all__"

    def clean_author(self):
        author = self.cleaned_data.get("author")
        if author.role != User.AUTHOR:
            self.add_error("author", "The author must have the role AUTHOR")
        return author

    def clean_subscriber(self):
        subscriber = self.cleaned_data.get("subscriber")
        if subscriber.role != User.SUBSCRIBER:
            self.add_error("subscriber", "The subscriber must have the role SUBSCRIBER")
        return subscriber
