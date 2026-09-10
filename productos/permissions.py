"""
from rest_framework import permissions

class GroupEditProductoPermission(permissions.BasePermission):
    # Permission custom para permitir acceso si es staff
    def has_permission(self, request, view):
        return request.user.is_staff
"""