from project.settings import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

INTERNAL_IPS = (
    '127.0.0.1',
)

CACHE_BACKEND = "locmem:///"
CACHE_TIMEOUT = 60 * 5
CACHE_PREFIX = "Z"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BUILDOUT_DIR, 'var', 'development.db'),
    }
}

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
}

MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

INSTALLED_APPS += (
    'django_extensions',
    'debug_toolbar',
)
