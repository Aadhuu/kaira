from django.http import HttpResponse
from django.shortcuts import render


def admin_required(function):
    def wrapper(request):
        if request.user.is_superuser == False:
            return render(request,'error.html')
        else:
            return function(request)
    return wrapper