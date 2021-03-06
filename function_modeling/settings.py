"""
Django settings for function_modeling project.

Generated by 'django-admin startproject' using Django 2.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '7e%@x%n*!bs1#d6eb*rlta^e3wgxv#h16eco(+au_r3v$n6p*3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

IMAGE_UPLOAD_DIR = "img"



# For RabbitMQ # RabbitMQ Broker
BROKER_URL = 'amqp://admin:admin@127.0.0.1:5672//'
#CELERY_RESULT_BACKEND = 'amqp://127.0.0.1'
# Celery Data Format
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
#CELERY_TIMEZONE = 'Asia/Kolkata'
BROKER_HOST                = '127.0.0.1'
BROKER_PORT                = 5672
BROKER_VHOST               = '/'
BROKER_USER                = 'admin'
BROKER_PASSWORD            = 'admin'

# Redis Result Backend
CELERY_RESULT_BACKEND      = 'redis'
CELERY_REDIS_HOST          = '127.0.0.1'
CELERY_REDIS_PORT          = 6379
#CELERY_REDIS_DB            = 1
#CELERY_REDIS_PASSWORD      = '*******'

"""
CELERY_SEND_EVENTS         = True
CELERY_TASK_RESULT_EXPIRES = 60 * 60 * 24 # 1 day
CELERY_ALWAYS_EAGER        = False
"""

#CELERY_IMPORTS = ("dashboard.tasks",)
#CELERY_REDIRECT_STDOUTS_LEVEL: 'INFO'
CELERY_BROKER_HEARTBEAT = 0

# For django redis
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            #"SOCKET_CONNECT_TIMEOUT": 5,  # in seconds
            #"SOCKET_TIMEOUT": 5,  # in seconds
        }
    }
}


ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
	'dashboard',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'function_modeling.urls'

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

WSGI_APPLICATION = 'function_modeling.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'function_db',
        'USER': 'admin',
        'PASSWORD': 'admin',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, "dashboard", "media")
#MEDIA_ROOT = 'C:\my_proj\function_modeling\dashboard\media'

MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(BASE_DIR, "dashboard", "static")
#STATIC_ROOT = 'C:\my_proj\function_modeling\dashboard\static'

"""


# static files will be stored in 'static' folder
STATIC_URL = '/static/'
STATICFILES_DIR = [
    BASE_DIR + '/static'
]
# media files will be stored in 'media' folder
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR + '/media'
"""
