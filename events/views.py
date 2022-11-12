from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from events.filter import EventFilter
from events.models import Event
from events.serializers import EventSerializer, ManagementEventSerializer
from events.permissions import EventPermissionList, EventPermissionObject
from users.permissions import IsManagement, IsSupport


class EventViewList(mixins.CreateModelMixin, mixins.ListModelMixin, GenericViewSet):
    filter_backends = [DjangoFilterBackend]
    filterset_class = EventFilter
    permission_classes = [IsAuthenticated, IsSupport, EventPermissionList]
    serializer_class = EventSerializer

    def get_queryset(self):
        return Event.objects.all()

    def list(self, request, *args, **kwargs):
        events_support = []
        for event in self.get_queryset():
            if event.support_contact == request.user:
                events_support.append(event)
        queryset = events_support

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class EventViewObject(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, GenericViewSet):
    permission_classes = [IsAuthenticated, IsSupport, EventPermissionObject]
    serializer_class = EventSerializer

    def get_queryset(self):
        return Event.objects.all()

    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)


class ManagementEventView(ModelViewSet):
    filter_backends = [DjangoFilterBackend]
    filterset_class = EventFilter
    permission_classes = [IsAuthenticated, IsManagement]
    serializer_class = ManagementEventSerializer

    def get_queryset(self):
        return Event.objects.all()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        message = f"Event <{instance.event_name}> has been deleted."
        self.perform_destroy(instance)
        return Response({"message": message}, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)
