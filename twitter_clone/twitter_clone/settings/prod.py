import os
import dj_database_url
from .base import *


SECRET_KEY = os.getenv(
    'DJANGO_SECRET_KEY',
    '^8ai-6gb!yyg182u3ahsi8a%c=)mb0xler7%0klh1mz!^snago;91_')
db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)

ALLOWED_HOSTS = ['wdc-w1-twitter-clone.herokuapp.com']
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
