from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "departamento_app"

urlpatterns = [
        # ------------------------------------------------------------------
        # CREAR TRABAJO
        # ------------------------------------------------------------------

        path('CrearTrabajo/',
                views.CrearTrabajo.as_view(),
                name='CrearTrabajo'),
        # ------------------------------------------------------------------
        # LISTAR TRABAJOS
        # ------------------------------------------------------------------

        path('ListarTrabajos/',
                views.ListarTrabajos.as_view(),
                name='ListarTrabajos'),
        # ------------------------------------------------------------------
        # VER TRABAJO
        # ------------------------------------------------------------------

        path('VerTrabajo/<pk>/',
                views.VerTrabajo.as_view(),
                name='VerTrabajo'),
        # ------------------------------------------------------------------
        # ACTUALIZAR TRABAJO
        # ------------------------------------------------------------------

        path('ActualizarTrabajo/<pk>/',
                views.ActualizarTrabajo.as_view(),
                name='ActualizarTrabajo'),
        # ------------------------------------------------------------------
        # ELIMINAR TRABAJO
        # ------------------------------------------------------------------

        path('EliminarTrabajo/<pk>/',
                views.EliminarTrabajo.as_view(),
                name='EliminarTrabajo'),
        # ------------------------------------------------------------------
        # CREAR DEPARTAMENTO
        # ------------------------------------------------------------------

        path('CrearDepartamento/',
                views.CrearDepartamento.as_view(),
                name='CrearDepartamento'),
        # ------------------------------------------------------------------
        # LISTAR DEPARTAMENTOS
        # ------------------------------------------------------------------

        path('ListarDepartamentos/',
                views.ListarDepartamentos.as_view(),
                name='ListarDepartamentos'),
        # ------------------------------------------------------------------
        # VER DEPARTAMENTO
        # ------------------------------------------------------------------

        path('VerDepartamento/<pk>/',
                views.VerDepartamento.as_view(),
                name='VerDepartamento'),
        # ------------------------------------------------------------------
        # ACTUALIZAR DEPARTAMENTO
        # ------------------------------------------------------------------

        path('ActualziarDepartamento/<pk>/',
                views.ActualziarDepartamento.as_view(),
                name='ActualziarDepartamento'),
        # ------------------------------------------------------------------
        # ELIMINAR DEPARTAMENTO
        # ------------------------------------------------------------------

        path('EliminarDepartamento/<pk>/',
                views.EliminarDepartamento.as_view(),
                name='EliminarDepartamento'),
        
]
