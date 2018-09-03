from django.shortcuts import render
from . import forms
# Create your views here.

def index(request):
    form = forms.ContactForm()
    return render(request,'main/index.html', {'form': form})
