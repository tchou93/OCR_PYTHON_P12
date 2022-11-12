from django.contrib import admin
from app.users.models import User


class UserAdmin(admin.ModelAdmin):
    model = User
    list_display = ("email", "last_name", "user_type")
    fields = ("username", "password", "first_name", "last_name", "email", "user_type", "is_active")


admin.site.register(User, UserAdmin)
