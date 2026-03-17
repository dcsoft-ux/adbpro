from django.urls import path
from . import views

app_name = "departamento_app"

urlpatterns = [
    # DEPARTAMENTOS
    path('departamentos/', views.ListarDepartamentos.as_view(), name='listar_departamentos'),
    path('departamentos/crear/', views.CrearDepartamento.as_view(), name='crear_departamento'),
    path('departamentos/<int:pk>/', views.VerDepartamento.as_view(), name='ver_departamento'),
    path('departamentos/<int:pk>/actualizar/', views.ActualizarDepartamento.as_view(), name='actualizar_departamento'),
    path('departamentos/<int:pk>/eliminar/', views.EliminarDepartamento.as_view(), name='eliminar_departamento'),

    # TRABAJOS
    path('trabajos/', views.ListarTrabajos.as_view(), name='listar_trabajos'),
    path('trabajos/crear/', views.CrearTrabajo.as_view(), name='crear_trabajo'),
    path('trabajos/<int:pk>/', views.VerTrabajo.as_view(), name='ver_trabajo'),
    path('trabajos/<int:pk>/actualizar/', views.ActualizarTrabajo.as_view(), name='actualizar_trabajo'),
    path('trabajos/<int:pk>/eliminar/', views.EliminarTrabajo.as_view(), name='eliminar_trabajo'),
]