from django_filters import rest_framework as filters, NumberFilter
from app.events.models import Event


class EventFilter(filters.FilterSet):
    first_name = filters.CharFilter(field_name="contract__client__first_name",
                                    lookup_expr="icontains")
    last_name = filters.CharFilter(field_name="contract__client__last_name",
                                   lookup_expr="icontains")
    email = filters.CharFilter(field_name="contract__client__email",
                               lookup_expr="iexact")
    year_event = NumberFilter(field_name="event_date", lookup_expr="year")
    min_year_event = NumberFilter(field_name="event_date", lookup_expr="year__gte")
    max_year_event = NumberFilter(field_name="event_date", lookup_expr="year__lte")
    month_event = NumberFilter(field_name="event_date", lookup_expr="month")
    min_month_event = NumberFilter(field_name="event_date", lookup_expr="month__gte")
    max_month_event = NumberFilter(field_name="event_date", lookup_expr="month__lte")
    day_event = NumberFilter(field_name="event_date", lookup_expr="day")
    min_day_event = NumberFilter(field_name="event_date", lookup_expr="day__gte")
    max_day_event = NumberFilter(field_name="event_date", lookup_expr="day__lte")

    class Meta:
        model = Event
        fields = ["first_name",
                  "last_name",
                  "email",
                  'year_event',
                  'min_year_event',
                  'max_year_event',
                  'month_event',
                  'min_month_event',
                  'max_month_event',
                  'day_event',
                  'min_day_event',
                  'max_day_event'
                  ]
