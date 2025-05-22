from rest_framework import serializers
from .models import TrainingProgram, Certificate

class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = '__all__'


class TrainingProgramSerializer(serializers.ModelSerializer):
    certificates = CertificateSerializer(many=True, read_only=True)

    class Meta:
        model = TrainingProgram
        fields = '__all__'
