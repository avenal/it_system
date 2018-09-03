from django.shortcuts import render
from main.forms import ContactForm
from throttle.decorators import throttle

# Create your views here.

def index(request):

    form = ContactForm()
    success = False
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            send_contact(request, form)
            form = ContactForm()
            success = True
    return render(request,'main/index.html', {'form': form, 'success':success})

@throttle(zone='default')
def send_contact(request, forms):
    forms.save(commit=True)
    return render(request,'main/index.html')
