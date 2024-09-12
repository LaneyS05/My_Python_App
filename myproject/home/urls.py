from django.urls import path
from .views import home_view, link_page, about_page, ask_ai

urlpatterns = [
    path('', home_view, name='home'),
    path('links/', link_page, name='link'),
    path('about/', about_page, name='about')
    path('ask-ai/', ask_ai, name='ask_ai'),
] 
