from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ("id", "email", "is_superuser", "is_staff", "is_active")
    list_filter = ("email", "is_superuser", "is_active",)
    fieldsets = (
        (None, {"fields": ("email", "password", 'last_name', 'first_name', 'patronymic')}),
        ("Permissions", {"fields": ("is_superuser", "is_staff", "is_active", "groups")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "password1", "password2", 'last_name', 'first_name', 'patronymic',
                "is_superuser", "is_staff", "is_active", "groups"
            )}
         ),
    )
    search_fields = ("email",)
    ordering = ("email",)
