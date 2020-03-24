from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse
# Create your views here.
def hi(request):
    return render(request,'Dentists/hi.html', {})

def contact(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']

        # send an email
        send_mail(
            message_name, # subject
            message,# message
            message_email,# from email
            ['appointsmile@gmail.com'],# To email
        )

        return render(request, 'Dentists/contact.html', {'message_name': message_name})
    else:
        return render(request,'Dentists/contact.html', {})