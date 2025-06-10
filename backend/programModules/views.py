from rest_framework import generics
from .models import programModules
from ..programModules.serializers import programModulesSerializer

# List and create programModules
class programModulesListCreateView(generics.ListCreateAPIView):
    queryset = programModules.objects.all()
    serializer_class = programModulesSerializer

# Retrieve, update or delete an individual Module
class programModulesDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = programModules.objects.all()
    serializer_class = programModulesSerializer