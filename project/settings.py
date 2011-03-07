import os

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '',
    }
}

TIME_ZONE = 'Europe/Vilnius'
LANGUAGE_CODE = 'lt'
SITE_ID = 1
USE_I18N = True
USE_L10N = True

PROJECT_DIR = os.path.realpath(os.path.dirname(__file__))
BUILDOUT_DIR = os.path.abspath(os.path.join(PROJECT_DIR, '..'))

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BUILDOUT_DIR, 'var', 'htdocs', 'static')
STATICFILES_DIRS = (
    os.path.join(BUILDOUT_DIR, 'project', 'static'),
)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BUILDOUT_DIR, 'var', 'htdocs', 'media')
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

SECRET_KEY = '8m86q=ycpwma&n1f0t-l)y(i&lx*aon=%!(uuv985a-t+a_bfw'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'project.urls'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_DIR, 'templates'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.request',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'south',
)

