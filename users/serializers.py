from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'user_type', 'email',
                  'phone', 'mobile', 'id', 'date_created', 'date_updated']
        extra_kwargs = {
            'id': {'read_only': True},
            'date_created': {'read_only': True},
            'date_update': {'read_only': True}
        }
