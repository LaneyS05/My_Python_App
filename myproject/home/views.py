from django.shortcuts import render
from django.core.mail import send_mail
from .models import ProjectLink
from django.conf import settings

def home_view(request):
    return render(request, 'home.html')

def link_page(request):
    links = ProjectLink.objects.all()
    return render(request, 'link.html', {'links': links})

def about_page(request):
    return render(request, 'about.html')


def send_email(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        send_mail(
            'New Contact Message',
            message,
            settings.DEFAULT_FROM_EMAIL,
            ['your-email@example.com'],  # Replace with your email
        )
    return render(request, 'email_sent.html')
