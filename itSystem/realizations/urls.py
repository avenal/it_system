from django.urls import path
from realizations import views

urlpatterns = [
    path('',views.realizations, name='realizations'),
]
