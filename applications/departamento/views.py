from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView,
)

from .serializer import DepartamentosSerializer
from .models import Departamento


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