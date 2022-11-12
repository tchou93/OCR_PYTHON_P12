from rest_framework.permissions import BasePermission


class ContractPermissionList(BasePermission):
    def has_permission(self, request, view):
        if request.method in ["GET", "POST"]:
            return request.user.user_type == "USER_SALES"

        return False


class ContractPermissionObject(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == "GET":
            return request.user.user_type == "USER_SALES" and obj.sales_contact == request.user

        if request.method == "PUT":
            return request.user.user_type == "USER_SALES" and obj.sales_contact == request.user \
                   and not obj.status

        return False
