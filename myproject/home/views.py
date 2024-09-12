from django.shortcuts import render
from django.core.mail import send_mail
from .models import ProjectLink
from django.conf import settings

PREDEFINED_QUESTIONS = {
    "tell me about the logo": "The logo on the home page was inspired by the Greek goddess Athena. Because the Dev enjoys Greek mythology so much she desided to incorporate it",
    "How do I message Laney": "Just press on the mail button at the bottom left corner of the screen",
    "Who is Laney": "Laney is a software developer who is currenly looking for a job. She is the person who made this Django app"
    "Has the Laney mady any apps for anyone": "Yes! She's currently working for a small company called Faith in Giving, where she's developing a React app for them."
}

def ask_ai(request):
    if request.method == 'POST':
        question = request.POST.get('question').lower()

        if question in PREDEFINED_QUESTIONS:
            response = PREDEFINED_QUESTIONS[question]
            else:
                response = "sorry the Dev only made me to where I can only answer specific questions"

            return JsonResponse({'response': response})
        return JsonResponse({'response': 'Invalid request method'}, status=400)

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
