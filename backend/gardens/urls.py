from django.urls import path
from . import views

urlpatterns = [
    path('analyze/', views.analyze_garden, name='analyze-garden'),
    path('plants/', views.get_plants, name='get-plants'),
]
