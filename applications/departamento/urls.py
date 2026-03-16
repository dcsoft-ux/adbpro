from django.urls import path
from . import views

app_name = "departamento_app"

urlpatterns = [
    path('departamentos/', views.ListarDepartamentos.as_view(), name='listar_departamentos'),
    path('departamentos/crear/', views.CrearDepartamento.as_view(), name='crear_departamento'),
    path('departamentos/<int:pk>/', views.VerDepartamento.as_view(), name='ver_departamento'),
    path('departamentos/<int:pk>/actualizar/', views.ActualizarDepartamento.as_view(), name='actualizar_departamento'),
    path('departamentos/<int:pk>/eliminar/', views.EliminarDepartamento.as_view(), name='eliminar_departamento'),
]