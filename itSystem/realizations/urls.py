from django.urls import path
from realizations.views import RealizationsView

urlpatterns = [
    path('',RealizationsView.as_view(), name='realizations'),
]
