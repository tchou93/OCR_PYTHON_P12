from rest_framework.permissions import BasePermission


class IsManagement(BasePermission):
    def has_permission(self, request, view):
        return request.user.user_type == "USER_MANAGEMENT"


class IsSaleSupport(BasePermission):
    def has_permission(self, request, view):
        return request.user.user_type in ["USER_SALES", "USER_SUPPORTS"]


class IsSale(BasePermission):
    def has_permission(self, request, view):
        return request.user.user_type == "USER_SALES"


class IsSupport(BasePermission):
    def has_permission(self, request, view):
        return request.user.user_type == "USER_SUPPORTS"
