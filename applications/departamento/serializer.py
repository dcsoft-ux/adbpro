from rest_framework import serializers
from .models import Departamento


class DepartamentosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = '__all__'