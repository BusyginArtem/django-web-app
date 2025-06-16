from django.shortcuts import render
from django.utils import timezone


def index(request):
    """
    Handles the main index.
    """
    context = {
        "user_name": getattr(request.user, "username", "Guest"),
        "request_method": request.method,
        "server_time": timezone.now().strftime("%Y-%m-%d %H:%M:%S"),
    }
    return render(request, "main/index.html", context)
