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
    TrabajosSerializer,
    DepartamentosSerializer,
)
# ------------------------------------------------------------------
# VISTAS A USAR
# ------------------------------------------------------------------

from django.views.generic import ListView, CreateView, UpdateView, DeleteView

# ------------------------------------------------------------------
# MODELOS
# ------------------------------------------------------------------
from .models import Departamento, Trabajo

# ------------------------------------------------------------------
# FORMULARIOS
# ------------------------------------------------------------------

from .forms import NuevoDepartamentoForm

# ------------------------------------------------------------------
# API CREAR UN TRABAJO
# ------------------------------------------------------------------
class CrearTrabajo(CreateAPIView):
    serializer_class = TrabajosSerializer

# ------------------------------------------------------------------
# API VER TODOS LOS TRABAJOS
# ------------------------------------------------------------------
class ListarTrabajos(ListAPIView):
    serializer_class = TrabajosSerializer
    def get_queryset(self):
        return Trabajo.objects.all()

# ------------------------------------------------------------------
# API VER TRABAJO
# ------------------------------------------------------------------
class VerTrabajo(RetrieveAPIView):
    serializer_class = TrabajosSerializer
    def get_queryset(self):
        return Trabajo.objects.all()

# ------------------------------------------------------------------
# API ACTUALIZAR TRABAJO
# ------------------------------------------------------------------
class ActualizarTrabajo(UpdateAPIView):
    serializer_class = TrabajosSerializer
    def get_queryset(self):
        return Trabajo.objects.all()


# ------------------------------------------------------------------
# API ELIMINAR TRABAJO
# ------------------------------------------------------------------
class EliminarTrabajo(DestroyAPIView):
    serializer_class = TrabajosSerializer
    def get_queryset(self):
        return Trabajo.objects.all()

# ------------------------------------------------------------------
# API CREAR UN DEPARTAMENTO
# ------------------------------------------------------------------
class CrearDepartamento(CreateAPIView):
    serializer_class = DepartamentosSerializer
# ------------------------------------------------------------------
# API LISTAR TODOS LOS DEPARTAMENTOS
# ------------------------------------------------------------------
class ListarDepartamentos(ListAPIView):
    serializer_class = DepartamentosSerializer
    def get_queryset(self):
        return Departamento.objects.all()
# ------------------------------------------------------------------
# API VER UN DEPARTAMENTO
# ------------------------------------------------------------------
class VerDepartamento(RetrieveAPIView):
    serializer_class = DepartamentosSerializer
    def get_queryset(self):
        return Departamento.objects.all()
# ------------------------------------------------------------------
# API ELIMINAR UN DEPARTAMENTO
# ------------------------------------------------------------------
class EliminarDepartamento(DestroyAPIView):
    serializer_class = DepartamentosSerializer
    def get_queryset(self):
        return Departamento.objects.all()
# ------------------------------------------------------------------
# API ACTUALIZAR UN DEPARTAMENTO
# ------------------------------------------------------------------
class ActualziarDepartamento(UpdateAPIView):
    serializer_class = DepartamentosSerializer
    def get_queryset(self):
        return Departamento.objects.all()
    
