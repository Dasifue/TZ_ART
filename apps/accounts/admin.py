"Accounts admin"

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

from .models import User, Subscribe
from .forms import UserCreationForm, SubscribeCreationForm

admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    "User admin class"
    add_form = UserCreationForm
    list_display = ("id", "email", "full_name", "role")
    list_display_links = ("id", "email", "full_name")
    list_filter = ("role",)
    search_fields = ("full_name", "email")
    ordering = ('id',)
    fieldsets = [
        (
            "Данные пользователя",
            {
                "fields": [
                    "full_name",
                    "email",
                    "role",
                ]
            }
        ),
    ]
    add_fieldsets = [
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'role', 'password1', 'password2')}
        ),
    ]
    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ('role',)
        return self.readonly_fields


@admin.register(Subscribe)
class SubscribeAdmin(admin.ModelAdmin):
    "Subscribe admin class"
    form = SubscribeCreationForm
    list_display = ("id", "author", "subscriber", "creation_date")
    list_display_links = ("id", "author", "subscriber")
    search_fields = ("id", "author__email", "subscriber__email")
