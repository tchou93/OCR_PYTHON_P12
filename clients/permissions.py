from rest_framework.permissions import BasePermission
from events.models import Event


class ClientPermissionList(BasePermission):
    def has_permission(self, request, view):
        if request.method == "GET":
            return True

        if request.method == "POST":
            return request.user.user_type == "USER_SALES"

        return False


class ClientPermissionObject(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == "GET":
            return (request.user.user_type == "USER_SALES" and obj.sales_contact == request.user) or \
                   (Event.objects.filter(support_contact=request.user, contract__client=obj).exists())

        if request.method in ["PUT"]:
            return request.user.user_type == "USER_SALES" and obj.sales_contact == request.user

        return False
