from django.urls import path

from app.clients.views import ClientViewList, ClientViewObject, ManagementClientView

client_list = ClientViewList.as_view({'get': 'list', 'post': 'create'})
client_detail = ClientViewObject.as_view({'get': 'retrieve', 'put': 'update'})
management_client_list = ManagementClientView.as_view({'get': 'list', 'post': 'create'})
management_client_detail = ManagementClientView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})

urlpatterns = [
    path('clients/', client_list, name='client-list'),
    path('clients/<int:pk>/', client_detail, name='client-detail'),
    path('management/clients/', management_client_list, name='management-client-list'),
    path('management/clients/<int:pk>/', management_client_detail, name='management-client-detail'),
]
