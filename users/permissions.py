from rest_framework.permissions import BasePermission


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role == 'admin'
        )


class IsAuthor(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role == 'author'
        )


class IsAdminOrAuthor(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role in ['admin', 'author']
        )
class IsAdminOrBlogOwner(BasePermission):

    def has_object_permission(self, request, view, obj):

        if request.user.role == 'admin':
            return True

        if request.user.role == 'author':
            return obj.user == request.user

        return False