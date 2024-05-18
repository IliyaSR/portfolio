from django.core.mail import send_mail
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

from portfolio.portfolio_pages.forms import ContactForm


# Create your views here.
def home(request):
    underline_home = ''
    if request:
        underline_home = 'Page is open'
    return render(request, template_name='home-page.html', context={"underline_home": underline_home})


def skills(request):
    underline_skills = ''
    if request:
        underline_skills = 'Page is open'
    return render(request, template_name='skills.html', context={"underline_skills": underline_skills})


def projects(request):
    underline_projects = ''
    if request:
        underline_projects = 'Page is open'
    return render(request, template_name='projects.html', context={"underline_projects": underline_projects})


def contact(request):
    underline_contact = ''
    if request:
        underline_contact = 'Page is open'

    if request.method == 'POST':
        name = request.POST.get('name')
        sender_email = request.POST.get('mail')
        message = request.POST.get('text')

        send_mail(
            f"You hove new mail from {name}, {sender_email}",
            message,
            sender_email,
            recipient_list=['iliaraev02@gmail.com']
        )

    form = ContactForm()

    return render(request, template_name='contact.html', context={"underline_contact": underline_contact, "form": form})
