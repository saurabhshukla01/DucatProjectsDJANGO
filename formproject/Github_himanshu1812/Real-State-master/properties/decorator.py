from django.core.exceptions import PermissionDenied
from .models import Profile


def user_authenticate(function):
    def wrap(request):
        profile=request.user
        if profile.is_seller==True:
            return function(request)
        else:
            raise PermissionDenied

    return wrap        
