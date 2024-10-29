# middleware.py
from django.http import HttpResponse

class FaviconRedirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path == '/favicon.ico':
            return HttpResponse(status=204)  # No Content response
        return self.get_response(request)
