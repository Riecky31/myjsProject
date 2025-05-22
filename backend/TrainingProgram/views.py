from rest_framework import generics
from .models import TrainingProgram, Certificate
from .serializers import TrainingProgramSerializer, CertificateSerializer

class TrainingProgramListCreateView(generics.ListCreateAPIView):
    queryset = TrainingProgram.objects.all()
    serializer_class = TrainingProgramSerializer

class TrainingProgramDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TrainingProgram.objects.all()
    serializer_class = TrainingProgramSerializer

class CertificateListCreateView(generics.ListCreateAPIView):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer

class CertificateDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer
