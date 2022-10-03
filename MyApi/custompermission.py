from rest_framework.permissions import BasePermission


class MyPermissionPost(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST':
            return True
        return False


class MyPermissionGet(BasePermission):

    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        return False
