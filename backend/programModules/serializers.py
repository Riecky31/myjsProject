# programModules/serializers.py
from rest_framework import serializers
from .models import programModules

class programModulesSerializer(serializers.ModelSerializer):
    program_name = serializers.CharField(source='trainingProgram.program_name', read_only=True)

    class Meta:
        model = programModules
        fields = ['id', 'title', 'link', 'program_name']
