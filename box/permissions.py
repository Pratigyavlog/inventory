from rest_framework import permissions

class IsAuthenticatedAndIsStaff(permissions.BasePermission):
  def has_permissions(self,request,view):
    if bool( request.user and request.user.is_authenticated 
    and request.user.is_staff and request.user.is_active 
    and not request.user.is_superuser):
      return True
    return False  

