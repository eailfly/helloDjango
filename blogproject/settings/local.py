from .common import *

SECRET_KEY = 'development-secret-key'
DEBUG = True
ALLOWED_HOSTS = ['*']

print(Path(__file__))

print(os.getenv('DJANGO_SETTINGS_MODULE'))
