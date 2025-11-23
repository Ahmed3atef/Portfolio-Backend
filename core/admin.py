from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
import random
from . import models

@admin.register(models.User)
class UserAdmin(BaseUserAdmin):
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("first_name" ,"last_name","password1", "password2", "email"),
            },
        ),
    )
    
    def save_model(self, request, obj, form, change):
        if not obj.username:
            random_digits = random.randint(100000, 999999)
            username = f"{obj.first_name.lower()}{obj.last_name.lower()}{random_digits}"
            obj.username = username
        super().save_model(request, obj, form, change)

