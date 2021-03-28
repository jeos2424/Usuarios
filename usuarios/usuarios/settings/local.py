from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'cxx*(@h4^d*xaqm2@=yn^g5(qnw6hz5$h1@4pgjq#wrj5&c61s'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': get_secret('DB_NAME'),
        'USER': get_secret('USER'),
        'PASSWORD': get_secret('PASSWORD'),
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'statics']

MEDIA_URL = '/media/'
MEDIA_ROOT = [BASE_DIR / 'media']