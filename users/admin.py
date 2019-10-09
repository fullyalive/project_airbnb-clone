from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


@admin.register(models.User)  # admin.site.register(models.User, CustomUserAdmin) 과 동일
class CustomUserAdmin(UserAdmin):

    """ Custom User Admin """

    list_display = ("superhost", "username", "email", "language", "currency")
    list_filter = ("superhost", "gender", "currency", "language")
    fieldsets = (
        (
            "사용자 기본 정보",
            {
                "fields": (
                    "superhost",
                    "avatar",
                    "gender",
                    "bio",
                    "birthdate",
                    "language",
                    "currency",
                )
            },
        ),
    ) + UserAdmin.fieldsets
