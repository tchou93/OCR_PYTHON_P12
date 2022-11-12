from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from app.users.models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        validators=[validate_password]
    )

    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'user_type', 'email',
                  'phone', 'mobile', 'id', 'date_created', 'date_updated']
        extra_kwargs = {
            'id': {'read_only': True},
            'date_created': {'read_only': True},
            'date_update': {'read_only': True},
            'password': {'write_only': True}
        }
