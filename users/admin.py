from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm, SetPasswordForm, PasswordChangeForm
from django.contrib.auth.hashers import make_password
from django.urls import path
from djoser.conf import User

from users.models import CustomUserForm

@admin.register(CustomUserForm)
class CustomUserFormAdmin(UserAdmin):
    list_display = ['username', 'password', ]

    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email", "gender", "owner_pet", "owner_tel", 'doctor_foto', 'doctor_job_title', )}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )



# admin.site.register(CustomUserForm)


