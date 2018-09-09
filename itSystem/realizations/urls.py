from django.urls import path
from realizations.views import RealizationsView, DetailedView

app_name = 'realizations'

urlpatterns = [
    path('',RealizationsView.as_view(), name='realizations'),
    path('<slug:slug>-<int:pk>',DetailedView.as_view(),name='details-realization' ),
]
