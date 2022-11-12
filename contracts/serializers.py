from rest_framework import serializers
from contracts.models import Contract


class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = ['sales_contact', 'client', 'date_created', 'date_updated', 'status', 'amount', 'payment_due', 'id']
        extra_kwargs = {
            'id': {'read_only': True},
            'sales_contact': {'read_only': True},
            'date_created': {'read_only': True},
            'date_update': {'read_only': True}
        }


class ManagementContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = ['sales_contact', 'client', 'date_created', 'date_updated', 'status', 'amount', 'payment_due', 'id']
        extra_kwargs = {
            'id': {'read_only': True},
            'date_created': {'read_only': True},
            'date_update': {'read_only': True}
        }
