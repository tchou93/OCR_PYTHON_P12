from django.urls import path
from events.views import EventView

event_list = EventView.as_view({'get': 'list','post': 'create'})
event_detail = EventView.as_view({'get': 'retrieve','put': 'update','delete': 'destroy'})

urlpatterns = [
    path('events/', event_list, name='event-list'),
    path('events/<int:pk>/', event_detail, name='event-detail'),
]
