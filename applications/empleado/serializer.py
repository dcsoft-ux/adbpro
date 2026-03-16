from rest_framework import serializers, pagination

from .models import(
    Habilidad,
    Empleado
)

class HabilidadesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habilidad
        fields = ('__all__')

class EmpleadosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = ('__all__')