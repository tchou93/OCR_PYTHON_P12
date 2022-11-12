from django_filters import rest_framework as filters, NumberFilter
from contracts.models import Contract


class ContractFilter(filters.FilterSet):
    first_name = filters.CharFilter(field_name="client__first_name",
                                    lookup_expr="icontains")
    last_name = filters.CharFilter(field_name="client__last_name",
                                   lookup_expr="icontains")
    email = filters.CharFilter(field_name="client__email",
                               lookup_expr="iexact")
    amount = NumberFilter(field_name="amount", lookup_expr="iexact")
    min_amount = NumberFilter(field_name="amount", lookup_expr="gte")
    max_amount = NumberFilter(field_name="amount", lookup_expr="lte")

    year_contract = NumberFilter(field_name="date_created", lookup_expr="year")
    min_year_contract = NumberFilter(field_name="date_created", lookup_expr="year__gte")
    max_year_contract = NumberFilter(field_name="date_created", lookup_expr="year__lte")
    month_contract = NumberFilter(field_name="date_created", lookup_expr="month")
    min_month_contract = NumberFilter(field_name="date_created", lookup_expr="month__gte")
    max_month_contract = NumberFilter(field_name="date_created", lookup_expr="month__lte")
    day_contract = NumberFilter(field_name="date_created", lookup_expr="day")
    min_day_contract = NumberFilter(field_name="date_created", lookup_expr="day__gte")
    max_day_contract = NumberFilter(field_name="date_created", lookup_expr="day__lte")

    class Meta:
        model = Contract
        fields = ["first_name",
                  "last_name",
                  "email",
                  "amount",
                  "min_amount",
                  "max_amount",
                  'year_contract',
                  'min_year_contract',
                  'max_year_contract',
                  'month_contract',
                  'min_month_contract',
                  'max_month_contract',
                  'day_contract',
                  'min_day_contract',
                  'max_day_contract'
                  ]
