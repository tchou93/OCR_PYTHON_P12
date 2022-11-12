from rest_framework.permissions import BasePermission


class EventPermissionList(BasePermission):
    def has_permission(self, request, view):
        return request.method == "GET"


class EventPermissionObject(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == "GET":
            return obj.support_contact == request.user
        if request.method == "PUT":
            return obj.support_contact == request.user and not obj.event_status

        return False
