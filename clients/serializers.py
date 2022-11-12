from rest_framework import serializers
from clients.models import Client


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['first_name', 'last_name', 'email',
                  'phone', 'mobile', 'company_name', 'date_created', 'date_updated', 'sales_contact', 'status', 'id']
        extra_kwargs = {
            'id': {'read_only': True},
            'sales_contact': {'read_only': True},
            'date_created': {'read_only': True},
            'date_update': {'read_only': True}
        }


class ManagementClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['first_name', 'last_name', 'email',
                  'phone', 'mobile', 'company_name', 'date_created', 'date_updated', 'sales_contact', 'status', 'id']
        extra_kwargs = {
            'id': {'read_only': True},
            'date_created': {'read_only': True},
            'date_update': {'read_only': True}
        }
