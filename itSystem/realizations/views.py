from django.shortcuts import render

# Create your views here.
def realizations(request):
    return render(request, 'realizations/index.html')
