from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from app.users.models import User
from app.users.permissions import IsManagement
from app.users.serializers import UserSerializer


class UserView(ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsManagement]

    def get_queryset(self):
        return User.objects.all()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        message = f"User <{instance.username}>({instance.user_type}) has been deleted."
        self.perform_destroy(instance)
        return Response({"message": message}, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)
