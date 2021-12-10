from django import forms
from django.forms import fields
from porto_app.models import ContactModel

class ContactForm(forms.ModelForm):
    class Meta: 
        models = ContactModel
