from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # API
    path('api/', include('applications.empleado.urls')),
    path('api/', include('applications.departamento.urls')),

    # Si quieres conservar las vistas HTML, deja esto al final
    path('', include('applications.inicio.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)