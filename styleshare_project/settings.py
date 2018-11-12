"""
Django settings for styleshare_project project.

Generated by 'django-admin startproject' using Django 2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'p+f&2ok8c1ko51%(g2!s(i7p$qp!i^!1#k6!p#mprdby*n54r)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [

    # Django Default

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # REST Framework
    'rest_framework',

    # O Auth (token authentication)
    'oauth2_provider',

    # CORS (Cross origin request) Allow
    'corsheaders',

    # Filtering & Ordering in API
    'django_filters',

    # created apps
    'user',
    'goods',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'styleshare_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'styleshare_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'django-styleshare',
#         'USER': 'root',
#         'PASSWORD': 'stylesharejcurve',
#         'HOST': 'database',
#         'PORT': 3306,
#     }
# }


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django-styleshare',
        'USER': os.environ['DB_USERNAME'],
        'PASSWORD': os.environ['DB_PASSWORD'],
        'HOST':  os.environ['DB_HOST'],   # Or an IP Address that your DB is hosted on
        'PORT': '3306',
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

# System User Model
AUTH_USER_MODEL = 'user.User'

# REST Framework settings

REST_FRAMEWORK = {

    # Authentication (REST framework does not authenticate user in middleware) :
    # https://stackoverflow.com/questions/24499304/why-does-django-rest-framework-provide-different-authentication-mechanisms
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # Our Django User Base OAuth Token is okay
        'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
    ),

    # Permission
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',
    ),

    # Parser
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.MultiPartParser',
        'rest_framework.parsers.FormParser',
    ),

    # Renderer ( REMOVED Browsable API )
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        # only in DEVELOPMENT MODE
        # 'rest_framework.renderers.BrowsableAPIRenderer',
    ),

    # Pagination
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,

    # Filtering / Searching / Ordering
    # https://www.django-rest-framework.org/api-guide/filtering/#djangofilterbackend
    'DEFAULT_FILTER_BACKENDS': (
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
        'django_filters.rest_framework.DjangoFilterBackend',
    ),
}

# OAuth2 Setting

oauth_scopes = {
        'read': 'Read scope',
        'write': 'Write scope',
        'groups': 'Access to your groups'
}

OAUTH2_PROVIDER = {
    # this is the list of available scopes (Customizable : 토큰에 얼마만큼 권한을 줄 것인지)
    'SCOPES': oauth_scopes
}

# corsheaders App Setting (between frontend and backend)

CORS_ORIGIN_ALLOW_ALL = False
CORS_ALLOW_CREDENTIALS = True

CORS_ORIGIN_WHITELIST = (
    # '<YOUR_DOMAIN>[:PORT]',
    'localhost:8080',
    '127.0.0.1:8080',

    'localhost:8000',
    '127.0.0.1:8000',

)

# Internal IP (for django debug toolbar)
# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html

INTERNAL_IPS = [
    '127.0.0.1',
    'localhost',
]
