import os

DEBUG = False
ALLOWED_HOSTS = ['3.68.80.16']

SECRET_KEY = os.environ.get('SECRET_KEY')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DBNAME'),
        'USER': os.environ.get('DBUSER'),
        'PASSWORD': os.environ.get('DBPASS'),
        'HOST': os.environ.get('DBHOST', '127.0.0.1'),
        'PORT': os.environ.get('DBPORT', '5432'),
    }
}

STATIC_ROOT = 'static/'