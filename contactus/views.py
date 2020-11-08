from django.shortcuts import render
from django.http.response import JsonResponse
from . import forms
from .models import Contact
from django.http import HttpResponse


# Create your views here.

def index(request):
    if request.method == "POST":
        '''
        name = request.POST.get('name')
        '''

        email = request.POST.get('email')
        '''
        phone = request.POST.get('phone')
        description = request.POST.get('description')
        contactlist = Contact.objects.all()
        '''

        '''looping through all contacts in list and comparing email'''

        '''for i in range(0 , len(contactlist)):
            if contactlist[i].email.lower() == email.lower():
                return JsonResponse(data={"message":"This email already exist"},status=500)'''
        
        form=forms.ContactForm(request.POST)
        if form.is_valid():
            form.save()
            
        else:
            return JsonResponse(data={"message":"this email already exist"},status=500)

        new_object=Contact.objects.get(email=email)
        
        '''
        new_object = Contact.objects.create(
            name=name,
            email=email,
            phone=phone,
            description=description
        )
        '''
        
        temp = {
            "id": new_object.id,
            "name": new_object.name,
            "email": new_object.email,
            "phone": new_object.phone,
            "description": new_object.description
        }

        return JsonResponse(temp)
    


    return render(request, 'index.html')


def submissions_view(request):
    contacts = Contact.objects.all()
    return render(request, 'submit.html', {'contacts': contacts})
