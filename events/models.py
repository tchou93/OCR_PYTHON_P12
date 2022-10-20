from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from users.models import User
from clients.models import Client


class Event(models.Model):
    event_name = models.CharField(_('event_name'), max_length=100)
    client = models.ForeignKey(to=Client,
                               on_delete=models.CASCADE,
                               limit_choices_to={"status": 'SUCCESS'})
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
    attendees = models.IntegerField()
    event_date = models.DateTimeField()
    notes = models.TextField(blank=True)


    def __str__(self):
        return f"[Event] {self.event_name} for {self.client}"
