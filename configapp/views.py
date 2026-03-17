import json
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

CONFIG_PATH = settings.BASE_DIR.child("runtime_config.json")


class RuntimeConfigView(APIView):
    def get(self, request):
        if CONFIG_PATH.exists():
            with open(CONFIG_PATH, "r", encoding="utf-8") as f:
                data = json.load(f)
        else:
            data = {
                "ALLOWED_HOSTS": [],
                "CORS_ALLOWED_ORIGINS": [],
                "API_BASE_URL": "http://127.0.0.1:8001/api",
            }
        return Response(data)

    def post(self, request):
        allowed_hosts = request.data.get("ALLOWED_HOSTS", [])
        cors_allowed_origins = request.data.get("CORS_ALLOWED_ORIGINS", [])
        api_base_url = request.data.get("API_BASE_URL", "http://127.0.0.1:8001/api")

        if not isinstance(allowed_hosts, list):
            return Response(
                {"error": "ALLOWED_HOSTS debe ser una lista"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if not isinstance(cors_allowed_origins, list):
            return Response(
                {"error": "CORS_ALLOWED_ORIGINS debe ser una lista"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if not isinstance(api_base_url, str):
            return Response(
                {"error": "API_BASE_URL debe ser texto"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        data = {
            "ALLOWED_HOSTS": allowed_hosts,
            "CORS_ALLOWED_ORIGINS": cors_allowed_origins,
            "API_BASE_URL": api_base_url.strip(),
        }

        with open(CONFIG_PATH, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        return Response({
            "message": "Configuración actualizada correctamente",
            "data": data,
        })