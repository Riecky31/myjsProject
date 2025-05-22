# Intern/urls.py
from django.urls import path
from .views import InternListCreateView, InternDetailView

urlpatterns = [
    path('', InternListCreateView.as_view(), name='intern-list'),
    path('<int:pk>/', InternDetailView.as_view(), name='intern-detail'),
]
