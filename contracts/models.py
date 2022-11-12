from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from clients.models import Client


class Contract(models.Model):
    sales_contact = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                                      on_delete=models.SET_NULL,
                                      null=True,
                                      limit_choices_to={"user_type": 'USER_SALES'},
                                      verbose_name=_('sales contact'))
    client = models.ForeignKey(to=Client,
                               on_delete=models.CASCADE,
                               limit_choices_to={"status": 'SUCCESS'})
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False, verbose_name="Contract Signed")
    amount = models.FloatField()
    payment_due = models.DateField(_("payment due"))

    def __str__(self):
        return f"{self.client} <=> {self.sales_contact}"
