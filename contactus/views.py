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
        contacts = Contact.objects.all()
        contactlist = list(contacts)
        
        '''looping through all contacts in list and comparing email'''
    
        
        for i in range(0,len(contactlist)):
            if contactlist[i].email.lower() == email.lower():
                return JsonResponse(data={"message":"This email already exist"},status=500)
            
        
        s=Contact.objects.create(
            name = name,
            email= email,
            phone = phone,
            description = description
        )
        
        
        temp = {
            "id" : s.id,
            "name" : s.name,
            "email" : s.email,
            "phone" : s.phone,
            "description" : s.description
        }
        
        
        return JsonResponse(temp)
    form = forms.ContactForm()
    return render(request, 'index.html', {'form': form})


def submissions_view(request):
    contacts = Contact.objects.all()
    return render(request, 'submit.html', {'contacts': contacts})

