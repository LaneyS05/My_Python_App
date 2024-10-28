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
import logging
from django.http import HttpResponse

logger = logging.getLogger(__name__)

def empty_favicon(request):
    logger.info("Favicon requested")
    return HttpResponse(status=204)  

urlpatterns = [
    path('favicon.ico', empty_favicon),  
    path('admin/', admin.site.urls),
    path('', include('home.urls')),  
]


