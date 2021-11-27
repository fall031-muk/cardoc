from rest_framework import permissions

class Custompermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST':
            return request.user.is_staff
        return request.user.is_authenticated