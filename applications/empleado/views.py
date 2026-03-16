from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView,
)

from .serializer import HabilidadesSerializer, EmpleadosSerializer
from .models import Empleado, Habilidad


# EMPLEADOS
class CrearEmpleado(CreateAPIView):
    serializer_class = EmpleadosSerializer
    queryset = Empleado.objects.all()


class ListarEmpleados(ListAPIView):
    serializer_class = EmpleadosSerializer
    queryset = Empleado.objects.all()


class VerEmpleado(RetrieveAPIView):
    serializer_class = EmpleadosSerializer
    queryset = Empleado.objects.all()


class ActualizarEmpleado(UpdateAPIView):
    serializer_class = EmpleadosSerializer
    queryset = Empleado.objects.all()


class EliminarEmpleado(DestroyAPIView):
    serializer_class = EmpleadosSerializer
    queryset = Empleado.objects.all()


# HABILIDADES
class CrearHabilidad(CreateAPIView):
    serializer_class = HabilidadesSerializer
    queryset = Habilidad.objects.all()


class ListarHabilidades(ListAPIView):
    serializer_class = HabilidadesSerializer
    queryset = Habilidad.objects.all()


class VerHabilidad(RetrieveAPIView):
    serializer_class = HabilidadesSerializer
    queryset = Habilidad.objects.all()


class ActualizarHabilidad(UpdateAPIView):
    serializer_class = HabilidadesSerializer
    queryset = Habilidad.objects.all()


class EliminarHabilidad(DestroyAPIView):
    serializer_class = HabilidadesSerializer
    queryset = Habilidad.objects.all()