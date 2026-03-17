from rest_framework import serializers
from .models import Departamento, Trabajo


class DepartamentosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = '__all__'


class TrabajosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trabajo
        fields = '__all__'