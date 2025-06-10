# Intern/urls.py
from django.urls import path
from ..programModules.views import programModulesListCreateView,  programModulesDetailView

urlpatterns = [
    path('',  programModulesListCreateView.as_view(), name=' programModules-list'),
    path('<int:pk>/',  programModulesDetailView.as_view(), name='programModules-detail'),
]
