from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, mixins
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from app.contracts.filter import ContractFilter
from app.contracts.serializers import ContractSerializer, ManagementContractSerializer
from app.contracts.models import Contract
from app.events.models import Event
from app.contracts.permissions import ContractPermissionList, ContractPermissionObject
from app.users.permissions import IsManagement, IsSale


class ContractViewList(mixins.CreateModelMixin, mixins.ListModelMixin, GenericViewSet):
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ["client__first_name", "client__last_name", "client__email", "client__company_name"]
    filterset_class = ContractFilter
    permission_classes = [IsAuthenticated, IsSale, ContractPermissionList]
    serializer_class = ContractSerializer

    def get_queryset(self):
        return Contract.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if request.user.user_type == "USER_SALES":
            queryset = Contract.objects.filter(sales_contact=request.user)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        data = serializer.save(sales_contact=self.request.user)
        if data.status:
            Event.objects.get_or_create(contract_id=data.id)


class ContractViewObject(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, GenericViewSet):
    permission_classes = [IsAuthenticated, IsSale, ContractPermissionObject]
    serializer_class = ContractSerializer

    def get_queryset(self):
        return Contract.objects.all()

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.status:
            message = f"Contract is signed and cannot be updated!"
            return Response({"message": message}, status=status.HTTP_400_BAD_REQUEST)
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)

    def perform_update(self, serializer):
        data = serializer.save(sales_contact=self.request.user)
        if data.status:
            Event.objects.get_or_create(contract_id=data.id)


class ManagementContractView(ModelViewSet):
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ["client__first_name", "client__last_name", "client__email", "client__company_name"]
    filterset_class = ContractFilter
    permission_classes = [IsAuthenticated, IsManagement]
    serializer_class = ManagementContractSerializer

    def get_queryset(self):
        return Contract.objects.all()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        message = f"Contract {instance.client} <=> {instance.sales_contact} has been deleted."
        self.perform_destroy(instance)
        return Response({"message": message}, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)

    def perform_create(self, serializer):
        data = serializer.save()
        if data.status:
            Event.objects.get_or_create()

    def perform_update(self, serializer):
        data = serializer.save()
        if data.status:
            Event.objects.get_or_create()
