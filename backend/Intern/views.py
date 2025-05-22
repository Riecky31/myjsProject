# views.py
from rest_framework import generics
from .models import Intern
from .serializers import InternSerializer

# List and create interns
class InternListCreateView(generics.ListCreateAPIView):
    queryset = Intern.objects.all()
    serializer_class = InternSerializer

# Retrieve, update or delete an individual intern
class InternDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Intern.objects.all()
    serializer_class = InternSerializer
