from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _

USERS_TYPE = [
    ('USER_MANAGEMENT', 'USER_MANAGEMENT'),
    ('USER_SALES', 'USER_SALES'),
    ('USER_SUPPORTS', 'USER_SUPPORTS')
]


class UserManager(BaseUserManager):
    def create_user(self, email, username, password, user_type, **other_fields):
        email = self.normalize_email(email)
        user = self.model(username=username,
                          email=email,
                          user_type=user_type,
                          **other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, username, password, **other_fields):
        other_fields.setdefault("is_superuser", True)
        other_fields.setdefault("is_staff", True)
        other_fields.setdefault("is_active", True)
        other_fields.setdefault("user_type", 'USER_MANAGEMENT')
        if other_fields.get("is_staff") is not True:
            raise ValueError("SuperUser must have is_staff=True.")
        if other_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        if other_fields.get("user_type") != 'USER_MANAGEMENT':
            raise ValueError("Superuser must have role of management")

        return self.create_user(email, username, password, **other_fields)


class User(AbstractUser):
    first_name = models.CharField(_("first name"), max_length=25)
    last_name = models.CharField(_("last name"), max_length=25)
    user_type = models.CharField(_("type"), max_length=50, choices=USERS_TYPE)
    email = models.EmailField()
    phone = models.CharField(_("phone"), max_length=20, blank=True)
    mobile = models.CharField(_("mobile"), max_length=20, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    object = UserManager()

    def __str__(self):
        return f"[{self.user_type}] {self.last_name}, {self.first_name} (Id: {self.id})"
