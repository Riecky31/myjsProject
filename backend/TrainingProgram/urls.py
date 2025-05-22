from django.urls import path
from .views import TrainingProgramListCreateView, TrainingProgramDetailView, CertificateListCreateView, CertificateDetailView

urlpatterns = [
    path('trainingPrograms/', TrainingProgramListCreateView.as_view(), name='training-program-list'),
    path('trainingPrograms/<int:pk>/', TrainingProgramDetailView.as_view(), name='training-program-detail'),
    path('certificates/', CertificateListCreateView.as_view(), name='certificate-list'),
    path('certificates/<int:pk>/', CertificateDetailView.as_view(), name='certificate-detail'),
]
