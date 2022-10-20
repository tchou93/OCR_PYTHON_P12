from django.urls import path

from clients.views import ClientView
client_list = ClientView.as_view({'get': 'list','post': 'create'})
client_detail = ClientView.as_view({'get': 'retrieve','put': 'update','delete': 'destroy'})

urlpatterns = [
    path('clients/', client_list, name='clients-list'),
    path('clients/<int:pk>/', client_detail, name='client-detail'),
]
