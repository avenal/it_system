from django.shortcuts import render
from realizations.models import Realization
from django.views.generic import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
def realizations(request):
    return render(request, 'realizations/index.html')

class RealizationsView(ListView):
    model = Realization
    template_name = 'realizations/index.html'
    context_object_name = 'realizations'
    paginate_by = 10
    queryset = Realization.objects.all()
