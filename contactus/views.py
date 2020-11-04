from django.shortcuts import render
from django.http.response import JsonResponse
from . import forms
from .models import Contact

# Create your views here.

def index(request):
    contacts = Contact.objects.all()
    if request.method == "POST":
        name= request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        description=request.POST.get('description')

        Contact.objects.create(
            name = name,
            email= email,
            phone = phone,
            description = description
        )
    form = forms.ContactForm()
    return render(request, 'index.html', {'form': form})


def submissions_view(request):
    contacts = Contact.objects.all()
    return render(request, 'submit.html', {'contacts': contacts})

