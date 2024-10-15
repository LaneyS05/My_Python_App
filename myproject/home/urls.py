from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('links/', views.link_page, name='links'),
    path('about/', views.about_page, name='about'),
    path('name/', views.name_page, name='name'),
]

