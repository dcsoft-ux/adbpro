# _______________ INICIO LIBRERIAS USADAS
import os
from unipath import Path
import json
from django.core.exceptions import ImproperlyConfigured

# _______________ FIN LIBRERIAS USADAS

# _______________ INICIO BASE DEL PROYECTO
BASE_DIR = Path(__file__).ancestor(3)
# _______________ FIN BASE DEL PROYECTO

# _______________ INICIO CONFIGURACION DINAMICA
RUNTIME_CONFIG_PATH = BASE_DIR.child("runtime_config.json")

runtime_config = {}
if os.path.exists(RUNTIME_CONFIG_PATH):
    with open(RUNTIME_CONFIG_PATH, "r", encoding="utf-8") as f:
        runtime_config = json.loads(f.read())
# _______________ FIN CONFIGURACION DINAMICA

# _______________ INICIO SECRET.JSON
with open("secret.json") as f:
    secret = json.loads(f.read())


def get_secret(secret_name, secrets=secret):
    try:
        return secrets[secret_name]
    except KeyError:
        msg = "la variable %s no existe" % secret_name
        raise ImproperlyConfigured(msg)
# _______________ FIN SECRET.JSON

# _______________ INICIO SECRET KEY
SECRET_KEY = get_secret('SECRET_KEY')
# _______________ FIN SECRET KEY

# _______ INICIO APPS
MY_APPS = (
    'applications.inicio',
    'applications.departamento',
    'applications.empleado',
    'configapp',
)

DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

THIRD_APPS = (
    'compressor',
    'rest_framework',
    'corsheaders',
)

INSTALLED_APPS = MY_APPS + DJANGO_APPS + THIRD_APPS
# _______ FIN APPS

# _________ INICIO MIDDLEWARE
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
# _________ FIN MIDDLEWARE

# _________ INICIO CORS
CORS_ALLOWED_ORIGINS = runtime_config.get(
    "CORS_ALLOWED_ORIGINS",
    [
        'http://localhost:5173',
        'http://127.0.0.1:5173',
    ]
)

CORS_ALLOW_METHODS = [
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
]
# _________ FIN CORS

# _________ INICIO ROOT_URLCONF
ROOT_URLCONF = 'abdpro.urls'
# _________ FIN ROOT_URLCONF

# _________ INICIO TEMPLATES
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR.child('templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
# _________ FIN TEMPLATES

# _________ INICIO WSGI_APPLICATION
WSGI_APPLICATION = 'abdpro.wsgi.application'
# _________ FIN WSGI_APPLICATION

# _________ INICIO AUTH_PASSWORD_VALIDATORS
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]
# _________ FIN AUTH_PASSWORD_VALIDATORS

# _________ INICIO DEFAULT_AUTO_FIELD
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# _________ FIN DEFAULT_AUTO_FIELD