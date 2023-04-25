# create a custom permissions
from rest_framework import permissions

class IsOwnerPermission(permissions.BasePermission):
    # function which return True/False whether the user has or hasn't the permission
    def has_object_permission(self ,request, view, object):
        # Check whether the user made the request is the owner or not  
        return request.user == object.owner
            
