from django import forms
from . import models


class ContactForm(forms.Form):

    name = forms.CharField(min_length=3, max_length=100, widget=forms.TextInput(attrs={'pattern':"[A-Za-z' ']+"}))
    email = forms.EmailField(max_length=20, error_messages={'invalid': "This is wrong"})
    phone= forms.CharField(required=False, widget=forms.TextInput(attrs={'pattern': '[0-9]{10}'}))
    description = forms.CharField(max_length=200, min_length=20, required=True, widget= forms.Textarea())
