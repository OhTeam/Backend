from config import settings
from .base import *

secrets = json.loads(open(SECRETS_DEV, 'rt').read())

set_config(secrets, module_name=__name__, start=True)
# print(set_config(secrets, module_name=__name__, start=True))
# print(getattr(sys.modules[__name__], 'DATABASES'))
# DATABASES = secrets['DATABASES']

secrets_base = json.loads(open(SECRETS_DEV, 'rt').read())
# set_config(secrets_base, module_name=__name__, start=False)

DATABASES = secrets_base['DATABASES']
DEBUG = True
ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    '.elasticbeanstalk.com',
    '.hongsj.kr',
    ]
WSGI_APPLICATION = 'config.wsgi.dev.application'

INSTALLED_APPS += [
    'django_extensions',
    'storages',
]

DEFAULT_FILE_STORAGE = 'config.storage.DefaultFileStorage'

# S3대신 EC2에서 정적파일을 제공 (프리티어의 put사용량 절감을 위해 )
# STATICFILES_STORAGE = 'config.storage.StaticFilesStorage'