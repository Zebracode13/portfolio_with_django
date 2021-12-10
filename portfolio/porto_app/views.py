from django.shortcuts import redirect, render
from porto_app.models import ContactModel

from django.views.generic import TemplateView, CreateView
# Create your views here.
from porto_app.forms import ContactForm
from porto_app.models import ContactModel

def home(request):
    return render(request, 'index.html')


    
