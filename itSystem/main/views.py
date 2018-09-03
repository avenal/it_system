from django.shortcuts import render
from . import forms
# Create your views here.

def index(request):
    form = forms.ContactForm()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            print("Validation Success!")
            print(form.cleaned_data['name'])
    return render(request,'main/index.html', {'form': form})
