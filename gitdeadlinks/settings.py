from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'linkchecker',  # Add your app here
]

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

DEBUG = True

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Directory for custom templates (optional)
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

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',  # Required
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # Required
    'django.contrib.messages.middleware.MessageMiddleware',  # Required
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# URL to use when referring to static files
STATIC_URL = '/static/'

# Directory to store static files (during collection for deployment)
STATIC_ROOT = BASE_DIR / 'staticfiles'  # Use this in production environments

# Additional locations of static files
STATICFILES_DIRS = [
    BASE_DIR / 'static',  # A directory named "static" in the project root
]

ROOT_URLCONF = 'gitdeadlinks.urls'
SECRET_KEY = '0p#5g6y44hgxr=wpslyl1pg%e(gr-in2#g2bgt0&4eho$#nd8_'
