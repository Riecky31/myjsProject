from rest_framework import generics
from .models import programModules
from .serializers import programModulesSerializer

class programModulesListCreateView(generics.ListCreateAPIView):
    queryset = programModules.objects.all()
    serializer_class = programModulesSerializer

class programModulesDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = programModules.objects.all()
    serializer_class = programModulesSerializer
