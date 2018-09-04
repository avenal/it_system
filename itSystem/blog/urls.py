from django.urls import path
from blog.views import BlogView, DetailedView

urlpatterns = [
    path('',BlogView.as_view(), name='blog'),
    path('<slug:slug>-<int:pk>',DetailedView.as_view(),name='details'),
]
