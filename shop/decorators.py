from django.http import HttpResponse


def admin_required(function):
    def wrapper(request):
        if request.user.is_superuser == False:
            return HttpResponse("Admin user only")
        else:
            return function(request)
    return wrapper