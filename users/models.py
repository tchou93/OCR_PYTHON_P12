from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _

USERS_TYPE = [
    ('USER_MANAGEMENT', 'USER_MANAGEMENT'),
    ('USER_SALES', 'USER_SALES'),
    ('USER_SUPPORTS', 'USER_SUPPORTS')
]


class UserManager(BaseUserManager):
    def create_user(self, email, username, user_type, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(email=self.normalize_email(email),
                          username=username,
                          user_type=user_type)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(email=email, username=username, password=password, user_type="USER_MANAGEMENT")
        user.is_admin = True
        user.save(using=self._db)

        return user


class User(AbstractUser):
    first_name = models.CharField(_("first name"), max_length=25)
    last_name = models.CharField(_("last name"), max_length=25)
    user_type = models.CharField(_("type"), max_length=50, choices=USERS_TYPE)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    phone = models.CharField(_("phone"), max_length=20, blank=True)
    mobile = models.CharField(_("mobile"), max_length=20, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    object = UserManager()

    def save(self, *args, **kwargs):

        if self.user_type == 'USER_MANAGEMENT':
            self.is_staff = True
            self.is_superuser = True

        self.set_password(self.password)
        return super(User, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.email}"
