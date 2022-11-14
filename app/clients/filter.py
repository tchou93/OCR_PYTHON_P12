from django_filters import rest_framework as filters
from app.clients.models import Client


class ClientFilter(filters.FilterSet):
    first_name = filters.CharFilter(field_name="first_name",
                                    lookup_expr="icontains")
    last_name = filters.CharFilter(field_name="last_name",
                                   lookup_expr="icontains")
    email = filters.CharFilter(field_name="email",
                               lookup_expr="iexact")

    class Meta:
        model = Client
        fields = ["first_name", "last_name", "email"]
