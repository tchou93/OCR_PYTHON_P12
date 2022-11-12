from django.db import models
from django.utils.translation import gettext_lazy as _
from users.models import User

CLIENT_STATUS = [
    ('IN_PROGRESS', 'IN_PROGRESS'),
    ('SUCCESS', 'SUCCESS'),
]


class Client(models.Model):
    first_name = models.CharField(_("first name"), max_length=25, blank=True)
    last_name = models.CharField(_("last name"), max_length=25, blank=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(_("phone"), max_length=20, blank=True)
    mobile = models.CharField(_("mobile"), max_length=20, blank=True)
    company_name = models.CharField(_("company name"), max_length=250, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    sales_contact = models.ForeignKey(to=User,
                                      on_delete=models.SET_NULL,
                                      null=True,
                                      limit_choices_to={"user_type": 'USER_SALES'})
    status = models.CharField(_("status"), default='IN_PROGRESS', max_length=50, choices=CLIENT_STATUS)

    def __str__(self):
        return f"{self.company_name}"
