from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import redirect
from .forms import ContactForm
from django.conf import settings


def home(request):
    return render(request, 'portfolio/home.html')


def sendEmail(request):
    if request.method == 'GET':
        form = ContactForm()
        print("GET REQUEST")
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            email = form.cleaned_data['email']
            merged_subject = "{}: {}".format(email, subject)
            message = form.cleaned_data['message']
            print("POST REQUEST. BEFORE TRY...")
            try:
                send_mail(merged_subject, message, settings.DEFAULT_FROM_EMAIL, ['testemail.python@yandex.com'])
                print("SEND_EMAIL WORKED")
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
                print("EXCEPT WORKED")
            return redirect('portfolio-success')
    return render(request, "portfolio/home.html", {'form': form})


def successView(request):
    return redirect(request, 'portfolio/home.html')
