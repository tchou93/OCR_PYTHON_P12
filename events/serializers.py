from rest_framework import serializers

from events.models import Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['event_name', 'contract', 'date_created', 'date_updated',
                  'support_contact', 'event_status', 'attendees', 'event_date', 'id']
        extra_kwargs = {
            'id': {'read_only': True},
            'contract': {'read_only': True},
            'support_contact': {'read_only': True},
            'date_created': {'read_only': True},
            'date_update': {'read_only': True}
        }


class ManagementEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['event_name', 'contract', 'date_created', 'date_updated',
                  'support_contact', 'event_status', 'attendees', 'event_date', 'id']
        extra_kwargs = {
            'id': {'read_only': True},
            'date_created': {'read_only': True},
            'date_update': {'read_only': True}
        }
