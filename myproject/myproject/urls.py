"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import logging
from django.http import HttpResponse

# Set up logging
logger = logging.getLogger(__name__)

# View to handle favicon requests
def empty_favicon(request):
    logger.info("Favicon requested, returning 204")
    return HttpResponse(status=204)  # No Content response

# URL configuration
urlpatterns = [
    path('favicon.ico', empty_favicon),  # Handle favicon requests
    path('admin/', admin.site.urls),
    path('', include('home.urls')),  # Main app routes
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)  # Serve static files

