import os
from .settings import *

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'b5ahuylglz7h(*i*#a4lu_l2u$zev3#8^*vsq2(p-rxyfv(ar@'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'test.db.sqlite3'),
    }
}

DEBUG = True

AUTH_PASSWORD_VALIDATORS = []

INTERNAL_IPS = ('127.0.0.1',)
