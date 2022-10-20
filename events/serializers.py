from rest_framework import serializers

from events.models import Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['event_name', 'client', 'date_created', 'date_updated',
                  'support_contact', 'event_status', 'attendees', 'event_date','id']
        extra_kwargs = {
            'id': {'read_only': True},
            'date_created': {'read_only': True},
            'date_update': {'read_only': True}
        }
