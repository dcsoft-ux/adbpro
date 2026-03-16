from django.shortcuts import render
from django.urls import reverse_lazy
# Create your views here.

# ------------------------------------------------------------------
# APIS
# ------------------------------------------------------------------
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    # DetailView
    RetrieveAPIView,
    # Delete
    DestroyAPIView,
    # Actualizar
    UpdateAPIView,
    # Recupera y actualiza
    RetrieveUpdateAPIView,
    # Recupera y elimina
    RetrieveDestroyAPIView,
)

from .serializer import (
    HabilidadesSerializer,
    EmpleadosSerializer,
)

# ------------------------------------------------------------------
# MODELOS
# ------------------------------------------------------------------
from .models import Empleado, Habilidad


# ------------------------------------------------------------------
# API CREAR UN EMPLEADO
# ------------------------------------------------------------------
class CrearEmpleado(CreateAPIView):
    serializer_class = EmpleadosSerializer

# ------------------------------------------------------------------
# API VER TODOS LOS EMPLEADOS
# ------------------------------------------------------------------
class ListarEmpleados(ListAPIView):
    serializer_class = EmpleadosSerializer
    def get_queryset(self):
        return Empleado.objects.all()

# ------------------------------------------------------------------
# API VER EMPLEADO
# ------------------------------------------------------------------
class VerEmpleado(RetrieveAPIView):
    serializer_class = EmpleadosSerializer
    def get_queryset(self):
        return Empleado.objects.all()

# ------------------------------------------------------------------
# API ACTUALZAR EMPLEADO
# ------------------------------------------------------------------
class ActualizarEmpleado(UpdateAPIView):
    serializer_class = EmpleadosSerializer
    def get_queryset(self):
        return Empleado.objects.all()

# ------------------------------------------------------------------
# API ELIMINAR EMPLEADOS
# ------------------------------------------------------------------
class EliminarEmpleado(DestroyAPIView):
    serializer_class = EmpleadosSerializer
    def get_queryset(self):
        return Empleado.objects.all()
    
# ------------------------------------------------------------------
# API CREAR UN HABILDIAD
# ------------------------------------------------------------------
class CrearHabilidad(CreateAPIView):
    serializer_class = HabilidadesSerializer

# ------------------------------------------------------------------
# API VER TODAS LAS HABILIDADES
# ------------------------------------------------------------------
class ListarHabilidades(ListAPIView):
    serializer_class = HabilidadesSerializer
    def get_queryset(self):
        return Habilidad.objects.all()

# ------------------------------------------------------------------
# API VER HABILIDAD
# ------------------------------------------------------------------
class VerHabilidad(RetrieveAPIView):
    serializer_class = HabilidadesSerializer
    def get_queryset(self):
        return Habilidad.objects.all()

# ------------------------------------------------------------------
# API ACTUALIZAR HABILIDAD
# ------------------------------------------------------------------
class ActualizarHabilidad(UpdateAPIView):
    serializer_class = HabilidadesSerializer
    def get_queryset(self):
        return Habilidad.objects.all()


# ------------------------------------------------------------------
# API ELIMINAR HABILIDAD
# ------------------------------------------------------------------
class EliminarHabilidad(DestroyAPIView):
    serializer_class = HabilidadesSerializer
    def get_queryset(self):
        return Habilidad.objects.all()