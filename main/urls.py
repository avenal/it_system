from django.urls import path
from main.views import MainView, ContactView

app_name = 'main'

urlpatterns = [
    path('',MainView.as_view(), name='index'),
    path('contact', ContactView.as_view(), name = 'contact'),
]
