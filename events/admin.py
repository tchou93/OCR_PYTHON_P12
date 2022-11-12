from django.contrib import admin
from events.models import Event


class EventAdmin(admin.ModelAdmin):
    model = Event
    list_display = ("event_name", "date_created", "event_status")
    fields = ("event_name", "contract", "support_contact", "event_status", "attendees", "event_date", "notes")


admin.site.register(Event, EventAdmin)
