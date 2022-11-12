from django.db import models
from django.utils.translation import gettext_lazy as _
from app.contracts.models import Contract
from app.users.models import User


class Event(models.Model):
    event_name = models.CharField(_('event_name'), max_length=100,blank=True)
    contract = models.OneToOneField(
        to=Contract,
        on_delete=models.CASCADE,
        null=True,
        limit_choices_to={"status": True}
    )
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    support_contact = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        limit_choices_to={"user_type": 'USER_SUPPORTS'},
        verbose_name=_('support contact')
    )
    event_status = models.BooleanField(default=False, verbose_name="Closed")
    attendees = models.IntegerField(blank=True, null=True)
    event_date = models.DateTimeField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.event_name}"
