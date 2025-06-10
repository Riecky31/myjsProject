from rest_framework import serializers
from ..programModules.models import programModules

class programModulesSerializer(serializers.ModelSerializer):
    class Meta:
        model = programModules
        fields = '__all__'
