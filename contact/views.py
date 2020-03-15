from django.shortcuts import render
from .forms import contactForm
from django.core.mail import send_mail
from django.conf import settings



def contact(request):
    title = 'Leave Message'
    form = contactForm(request.POST or None)
    confirm_message = None

    if form.is_valid():
        
        name = form.cleaned_data['name']
        message = form.cleaned_data['discussion']
        subject = 'Message from FSK SALON AND ACADEMY'
        message = '%s %s', (message, name)
        emailFrom = [form.cleaned_data['email']]
        emailTo = [settings.EMAIL_HOST_USER]
        send_mail( subject, message, emailFrom, emailTo, fail_silently=True)
        title = "Thanks"
        confirm_message = "Our staff will call back later and answer your questions."
        form = None
        
    context = { 'title' : title, 'form' : form, 'confirm_message' : confirm_message }
    template = "contact.html"
    return render(request, template, context)
