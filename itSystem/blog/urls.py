from django.urls import path
from blog.views import BlogView, DetailedView

app_name = 'blog'

urlpatterns = [
    path('',BlogView.as_view(), name='blog'),
    path('<slug:slug>-<int:pk>',DetailedView.as_view(),name='details-blog'),
]
