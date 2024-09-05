from django.urls import path
from .views import home_view, link_page, about_page

urlpatterns = [
    path('', home_view, name='home'),
    path('links/', link_page, name='link'),
    path('about/', about_page, name='about')
] 
