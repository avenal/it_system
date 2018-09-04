from django.shortcuts import render
from blog.models import BlogEntry
from django.views.generic import ListView
from django.views.generic.detail import DetailView
# Create your views here.
def blog(request):
    return render(request,'blog/index.html')

class BlogView(ListView):
    model = BlogEntry
    template_name = 'blog/index.html'
    context_object_name = 'blog_entries'
    paginate_by = 2
    queryset = BlogEntry.objects.all().order_by('-pk')

class DetailedView(DetailView):
    model = BlogEntry
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
