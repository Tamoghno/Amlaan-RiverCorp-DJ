from django.shortcuts import render
from WebPage.models import Contact
from django.contrib import messages

# Create your views here.


def home(request):
    return render(request, 'home.html')


def contact(request):

    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        if len(name) < 3 or len(email) < 10 or len(subject) < 15 or len(message) < 5:
            messages.error(request, "Please fill out the form correctly.")
        else:
            coNtact = Contact(name=name, email=email,
                              subject=subject, message=message)
            coNtact.save()
            messages.success(request, "Submitted Successfully!")
    return render(request, 'home.html')


def about(request):
    return render(request, 'aboutus.html')
