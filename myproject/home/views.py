#home/views.py
from django.shortcuts import render, redirect
from .models import ProjectLink, Name
from django.core.mail import send_mail
from django.conf import settings

def home_view(request):
    return render(request, 'home/home.html')

def link_page(request):
    links = ProjectLink.objects.all()
    return render(request, 'home/link.html', {'links': links})


def about_page(request):
    return render(request, 'home/about.html')

def name_page(request):
    if request.method == 'POST':
        user_name = request.POST.get('name', '').strip()
        max_length = 10

        if not user_name.isalpha():
            return render(request, 'name_page.html', {'error': "Numbers are not allowed."})
        elif user_name.isupper() or user_name.islower():
            return render(request, 'name_page.html', {'error': "Please capitalize your name properly."})
        elif len(user_name) > max_length:
            return render(request, 'name_page.html', {'error': "Your name is too long."})
        else:
            Name.objects.create(name=user_name)
            return redirect('home')  

    return render(request, 'name.html')

def send_email(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        user_email = request.POST.get('email')  

        send_mail(
            'New Contact Message',
            message,
            user_email,
            ['laney.staggs05@gmail.com'],
        )
        return render(request, 'email_sent.html')
    
    return render(request, 'email_sent.html')
