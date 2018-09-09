from django.shortcuts import render
from realizations.models import Realization
from django.views.generic import ListView
from django.views.generic.detail import DetailView
# Create your views here.
#from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class RealizationsView(ListView):
    model = Realization
    template_name = 'realizations/index.html'
    context_object_name = 'realizations'
    paginate_by = 6
    queryset = Realization.objects.all().order_by('-pk')

class DetailedView(DetailView):
    model = Realization
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
