from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to edit their own profile"""

    def has_object_permission(self,request,views,obj):
        """Check user is trying to edit their own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return request.user.id == obj.id

class UpdateOwnProfileFeed(permissions.BasePermission):
    """Allow user to edit their own feed"""

    def has_object_permission(self,request,views,obj):
        """Check the user is trying to edit their own feed"""
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return request.user.id == obj.user_profile.id