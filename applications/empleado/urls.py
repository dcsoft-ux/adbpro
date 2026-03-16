from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "empleado_app"

urlpatterns = [
    # ------------------------------------------------------------------
    # CREAR EMPLEADO
    # ------------------------------------------------------------------

    path('CrearEmpleado/',
        views.CrearEmpleado.as_view(),
        name='CrearEmpleado'),
    # ------------------------------------------------------------------
    # VER TODOS LOS EMPLEADOS
    # ------------------------------------------------------------------

    path('ListarEmpleados/',
        views.ListarEmpleados.as_view(),
        name='ListarEmpleados'),

    # ------------------------------------------------------------------
    # VER EMPLEADO
    # ------------------------------------------------------------------

    path('VerEmpleado/<pk>',
        views.VerEmpleado.as_view(),
        name='VerEmpleado'),
    # ------------------------------------------------------------------
    # ACTUALIZAR EMPLEADO
    # ------------------------------------------------------------------

    path('ActualizarEmpleado/<pk>',
        views.ActualizarEmpleado.as_view(),
        name='ActualizarEmpleado'),

    # ------------------------------------------------------------------
    # ELIMINAR EMPLEADO
    # ------------------------------------------------------------------

    path('EliminarEmpleado/<pk>',
        views.EliminarEmpleado.as_view(),
        name='EliminarEmpleado'),
    # ------------------------------------------------------------------
    # CREAR HABILIDAD
    # ------------------------------------------------------------------

    path('CrearHabilidad/',
        views.CrearHabilidad.as_view(),
        name='CrearHabilidad'),
    # ------------------------------------------------------------------
    # VER TODOS LAS HABILIDADES
    # ------------------------------------------------------------------

    path('ListarHabilidades/',
        views.ListarHabilidades.as_view(),
        name='ListarHabilidades'),

    # ------------------------------------------------------------------
    # VER HABILIDAD
    # ------------------------------------------------------------------

    path('VerHabilidad/<pk>',
        views.VerHabilidad.as_view(),
        name='VerHabilidad'),
    # ------------------------------------------------------------------
    # ACTUALIZAR HABILIDAD
    # ------------------------------------------------------------------

    path('ActualizarHabilidad/<pk>',
        views.ActualizarHabilidad.as_view(),
        name='ActualizarHabilidad'),

    # ------------------------------------------------------------------
    # ELIMINAR HABILIDAD
    # ------------------------------------------------------------------

    path('EliminarHabilidad/<pk>',
        views.EliminarHabilidad.as_view(),
        name='EliminarHabilidad'),

]
