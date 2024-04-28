from .base import *
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'bdemma',
        'USER': 'manuel',
        'PASSWORD': 'computador01',
        'HOST': 'localhost',
        'PORT': '5432',  
    }
}

