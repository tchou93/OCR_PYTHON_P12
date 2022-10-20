from django.urls import path

from contracts.views import ContractView
contract_list = ContractView.as_view({'get': 'list','post': 'create'})
contract_detail = ContractView.as_view({'get': 'retrieve','put': 'update','delete': 'destroy'})

urlpatterns = [
    path('contracts/', contract_list, name='contracts-list'),
    path('contracts/<int:pk>/', contract_detail, name='contract-detail'),
]
