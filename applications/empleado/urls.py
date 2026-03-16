from django.urls import path
from . import views

app_name = "empleado_app"

urlpatterns = [
    # EMPLEADOS
    path('empleados/', views.ListarEmpleados.as_view(), name='listar_empleados'),
    path('empleados/crear/', views.CrearEmpleado.as_view(), name='crear_empleado'),
    path('empleados/<int:pk>/', views.VerEmpleado.as_view(), name='ver_empleado'),
    path('empleados/<int:pk>/actualizar/', views.ActualizarEmpleado.as_view(), name='actualizar_empleado'),
    path('empleados/<int:pk>/eliminar/', views.EliminarEmpleado.as_view(), name='eliminar_empleado'),

    # HABILIDADES
    path('habilidades/', views.ListarHabilidades.as_view(), name='listar_habilidades'),
    path('habilidades/crear/', views.CrearHabilidad.as_view(), name='crear_habilidad'),
    path('habilidades/<int:pk>/', views.VerHabilidad.as_view(), name='ver_habilidad'),
    path('habilidades/<int:pk>/actualizar/', views.ActualizarHabilidad.as_view(), name='actualizar_habilidad'),
    path('habilidades/<int:pk>/eliminar/', views.EliminarHabilidad.as_view(), name='eliminar_habilidad'),
]