from rest_framework.permissions import BasePermission


class IsSeller(BasePermission):

    def has_permission(self, request, view):

        if request.method in ["GET", "HEAD", "OPTIONS"]:
            return True

        return (
            request.user.is_authenticated
            and request.user.role == "seller"
        )

class IsOwnerSeller(BasePermission):

    def has_object_permission(self, request, view, obj):

        if request.method in ["GET", "HEAD", "OPTIONS"]:
            return True

        return (
            request.user.is_authenticated
            and hasattr(request.user, "seller_profile")
            and obj.seller == request.user.seller_profile
        )