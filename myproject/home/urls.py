#home/urls.py
from django.urls import path
from . import views  # Import views from the current package

urlpatterns = [
    path('', views.home_view, name='home'),
    path('links/', views.link_page, name='links'),
    path('about/', views.about_page, name='about'),
    path('name/', views.name_page, name='name'),
    path('send-email/', views.send_email, name='send_email'),  # Assuming you have this URL
]
