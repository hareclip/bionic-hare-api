from django.contrib.auth import authenticate
from rest_framework.response import Response

def auth_decorator(roles):
    """Authentication decorator
    """
    def decorator(function):
        def wrapper(request, *args, **kwargs):
            username = request.POST.get('username')
            if username == None:
                return Response('username is required', 400)
            password = request.POST.get('password')
            if password == None:
                return Response('password is required', 400)

            user = authenticate(username=username, password=password)
            if user == None:
                return Response('user is unauthorized', 401)

            # Validate roles
            if 2 in roles and not user.is_staff:
                return Response('user is not staff', 403)
            if 3 in roles and not user.is_superuser:
                return Response('user is not superuser', 403)

            request.user = user
            return function(request, *args, **kwargs)
        return wrapper
    return decorator
