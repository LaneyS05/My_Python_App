from django.shortcuts import render
from .models import ProjectLink

def home_view(request):
    return render(request, 'home.html')

def link_page(request):
    links = ProjectLink.objects.all()
    return render(request, 'link.html', {'links': links})
