from django.shortcuts import render
from django.http.response import JsonResponse
from . import forms
from .models import Contact
from django.http import HttpResponse

# Create your views here.

def index(request):
    
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
        contacts = Contact.objects.all()
        temp = list(contacts)
        print(temp[-1].id,temp[-1].email)
        return HttpResponse("id=" + str(temp[-1].id) + "\nname="+temp[-1].name+"\nemail="+temp[-1].email+ "\nphone="+ temp[-1].phone + "\ndescription=" +temp[-1].description )
    form = forms.ContactForm()
    return render(request, 'index.html', {'form': form})


def submissions_view(request):
    contacts = Contact.objects.all()
    return render(request, 'submit.html', {'contacts': contacts})

