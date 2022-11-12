from django.urls import path
from contracts.views import ContractViewList, ContractViewObject, ManagementContractView

contract_list = ContractViewList.as_view({'get': 'list', 'post': 'create'})
contract_detail = ContractViewObject.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})
management_contract_list = ManagementContractView.as_view({'get': 'list', 'post': 'create'})
management_contract_detail = ManagementContractView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})

urlpatterns = [
    path('contracts/', contract_list, name='contracts-list'),
    path('contracts/<int:pk>/', contract_detail, name='contract-detail'),
    path('management/contracts/', management_contract_list, name='management-contract-list'),
    path('management/contracts/<int:pk>/', management_contract_detail, name='management-contract-detail')
]
