from django.urls import path
from app.events.views import EventViewList, EventViewObject, ManagementEventView

event_list = EventViewList.as_view({'get': 'list'})
event_detail = EventViewObject.as_view({'get': 'retrieve', 'put': 'update'})
management_event_list = ManagementEventView.as_view({'get': 'list', 'post': 'create'})
management_event_detail = ManagementEventView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})


urlpatterns = [
    path('events/', event_list, name='event-list'),
    path('events/<int:pk>/', event_detail, name='event-detail'),
    path('management/events/', management_event_list, name='management-event-list'),
    path('management/events/<int:pk>/', management_event_detail, name='management-event-detail'),
]
