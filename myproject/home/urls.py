from django.shortcuts import render

def home_view(request):
    return render(request, 'home.html')  # Ensure this template exists

def link_page(request):
    return render(request, 'links.html')  # Ensure this template exists

def about_page(request):
    return render(request, 'about.html')  # Ensure this template exists

def name_page(request):
    return render(request, 'name.html')  # Ensure this template exists
