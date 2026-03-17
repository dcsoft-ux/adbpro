from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("applications.empleado.urls")),
    path("api/", include("applications.departamento.urls")),
    path("api/", include("configapp.urls")),
    path("", include("applications.inicio.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)