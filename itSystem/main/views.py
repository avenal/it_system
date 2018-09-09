from django.shortcuts import render
from main.forms import ContactForm
from throttle.decorators import throttle
from django.views import View
# Create your views here.
'''
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
'''


class MainView(View):
    form_class = ContactForm
    initial = {'key':'value'}
    template_name = 'main/index.html'
    success = False
    def get(self, request, *args, **kwargs):
        success = False
        form = self.form_class(initial = self.initial)
        return render(request, self.template_name,{'form':form})

    @throttle(zone='default')
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save(commit=True)
            form = self.form_class(initial = self.initial)
            success = True
        return render(request, self.template_name, {'form': form, 'success':success})

class ContactView(View):
    form_class = ContactForm
    initial = {'key':'value'}
    template_name = 'main/contact.html'
    success = False
    def get(self, request, *args, **kwargs):
        success = False
        form = self.form_class(initial = self.initial)
        return render(request, self.template_name,{'form':form})

    @throttle(zone='default')
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save(commit=True)
            form = self.form_class(initial = self.initial)
            success = True
        return render(request, self.template_name, {'form': form, 'success':success})
