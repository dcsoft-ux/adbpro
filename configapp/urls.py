from django.urls import path
from .views import RuntimeConfigView

urlpatterns = [
    path("configuracion/", RuntimeConfigView.as_view(), name="runtime_config"),
]