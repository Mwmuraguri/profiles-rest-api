from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow a user to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user"""
        if request.method in permisions.SAFE_METHODS:
            return True

        return obj.id == request.user.id
