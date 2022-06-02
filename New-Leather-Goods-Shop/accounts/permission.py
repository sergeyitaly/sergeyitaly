from rest_framework.permissions import BasePermission,SAFE_METHODS

#Object-level permission to only allow owners of an object to edit it
class IsOwnerProfileOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.user==request.user