from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from app.clients.models import Client
from app.events.models import Event
from app.clients.serializers import ClientSerializer, ManagementClientSerializer
from app.clients.permissions import ClientPermissionList, ClientPermissionObject
from app.users.permissions import IsSaleSupport, IsManagement
from app.clients.filter import ClientFilter


class ClientViewList(mixins.CreateModelMixin, mixins.ListModelMixin, GenericViewSet):
    filter_backends = DjangoFilterBackend
    filterset_class = ClientFilter
    permission_classes = [IsAuthenticated, ClientPermissionList, IsSaleSupport]
    serializer_class = ClientSerializer

    def get_queryset(self):
        return Client.objects.all()

    def perform_create(self, serializer):
        serializer.save(sales_contact=self.request.user)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if request.user.user_type == "USER_SUPPORTS":
            clients_support = []
            for client in self.get_queryset():
                if Event.objects.filter(support_contact=request.user, contract__client=client).exists():
                    clients_support.append(client)
            queryset = clients_support
        elif request.user.user_type == "USER_SALES":
            queryset = Client.objects.filter(sales_contact=request.user)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ClientViewObject(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, GenericViewSet):
    permission_classes = [IsAuthenticated, ClientPermissionObject, IsSaleSupport]
    serializer_class = ClientSerializer

    def get_queryset(self):
        return Client.objects.all()

    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)


class ManagementClientView(ModelViewSet):
    filter_backends = [DjangoFilterBackend]
    filterset_class = ClientFilter
    permission_classes = [IsAuthenticated, IsManagement]
    serializer_class = ManagementClientSerializer

    def get_queryset(self):
        return Client.objects.all()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        message = f"Client <{instance.company_name}> has been deleted."
        self.perform_destroy(instance)
        return Response({"message": message}, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)
