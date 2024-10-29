import logging
from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin  # Import MiddlewareMixin

logger = logging.getLogger(__name__)

class FaviconMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path == '/favicon.ico':
            logger.info("Favicon requested, returning 204")
            return HttpResponse(status=204)  # No Content
