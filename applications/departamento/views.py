from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView,
)

from .serializer import DepartamentosSerializer, TrabajosSerializer
from .models import Departamento, Trabajo


# DEPARTAMENTOS
class CrearDepartamento(CreateAPIView):
    serializer_class = DepartamentosSerializer
    queryset = Departamento.objects.all()


class ListarDepartamentos(ListAPIView):
    serializer_class = DepartamentosSerializer
    queryset = Departamento.objects.all()


class VerDepartamento(RetrieveAPIView):
    serializer_class = DepartamentosSerializer
    queryset = Departamento.objects.all()


class ActualizarDepartamento(UpdateAPIView):
    serializer_class = DepartamentosSerializer
    queryset = Departamento.objects.all()


class EliminarDepartamento(DestroyAPIView):
    serializer_class = DepartamentosSerializer
    queryset = Departamento.objects.all()


# TRABAJOS
class CrearTrabajo(CreateAPIView):
    serializer_class = TrabajosSerializer
    queryset = Trabajo.objects.all()


class ListarTrabajos(ListAPIView):
    serializer_class = TrabajosSerializer
    queryset = Trabajo.objects.all()


class VerTrabajo(RetrieveAPIView):
    serializer_class = TrabajosSerializer
    queryset = Trabajo.objects.all()


class ActualizarTrabajo(UpdateAPIView):
    serializer_class = TrabajosSerializer
    queryset = Trabajo.objects.all()


class EliminarTrabajo(DestroyAPIView):
    serializer_class = TrabajosSerializer
    queryset = Trabajo.objects.all()