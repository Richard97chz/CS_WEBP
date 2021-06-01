
from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE':'django.db.backends.postgresql_psycopg2',
        'NAME':get_secret('DB_NAME'),
        'USER':get_secret('USER'),
        'PASSWORD':get_secret('PASSWORD'),
        'HOST':'localhost',
        'PORT':'5433',    #PONGO EL 5433, porque a veces postgre no puede usar su puerto por defecto
    }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS=[BASE_DIR.child('static')]  #dentro de base dir busca carpeta llamada static

MEDIA_URL='/media/'
MEDIA_ROOT=BASE_DIR.child('media') #child: como si fuera un hijo del BASE_DIR