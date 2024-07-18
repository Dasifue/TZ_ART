"Account forms. Using for django admin site"

from django import forms

from .models import User, Subscribe


class UserCreationForm(forms.ModelForm):
    "Registartion Form"
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        "Meta class"
        model = User
        fields = [
            'email',
            'role'
        ]

    def clean_password2(self) -> str:
        "method validates passwords matching"
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            self.add_error("password1", "Passwords didn't match")
            self.add_error("password2", "Passwords didn't match")
        return password2

    def save(self, commit: bool = True) -> User:
        "method using for user creation and password setup"
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class SubscribeCreationForm(forms.ModelForm):
    "Subscribe creation form"

    class Meta:
        "Meta class"
        model = Subscribe
        fields = "__all__"

    def clean_author(self) -> User:
        "method validates author role"
        author = self.cleaned_data.get("author")
        if author.role != User.AUTHOR:
            self.add_error("author", "The author must have the role AUTHOR")
        return author

    def clean_subscriber(self) -> User:
        "method validates subscriber role"
        subscriber = self.cleaned_data.get("subscriber")
        if subscriber.role != User.SUBSCRIBER:
            self.add_error("subscriber", "The subscriber must have the role SUBSCRIBER")
        return subscriber
