from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS


class CheckUserCreate(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.user_role == 'simpleUser':
            return False
        return True


class CheckHotelOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
       return request



class CheckRoomCreate(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.user_role == 'simpleUser':
            return False
        return True


class CheckReviewUser(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.user_role == 'simpleUser':
            return True
        return False


class CheckReviewEDIT(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user == obj.user_name