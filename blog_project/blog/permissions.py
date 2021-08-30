from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS

class BlogPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        group = None
        if isinstance(request.user, User):
            group = request.user.groups.all()[0].name
        if request.method in SAFE_METHODS:
            return True
        if group == 'admin' and request.method in ['GET','POST','PUT','DELETE']:
            return True
