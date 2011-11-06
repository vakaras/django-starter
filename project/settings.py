# coding: utf-8

# DO NOT MODIFY! This file is generated from /home/sirex/devel/ubuntu-lt-django-lightweight/config/settings.py template.

import os

PROJECT_DIR = os.path.realpath(os.path.dirname(__file__))
BUILDOUT_DIR = os.path.abspath(os.path.join(PROJECT_DIR, '..'))

# Make external tools like SASS and Compass available in PATH.
path = os.environ['PATH'].split(':')
path.append(os.path.join(BUILDOUT_DIR, 'bin'),)
os.environ['PATH'] = ':'.join(path)


s = {
    'PREFIX': os.path.join(BUILDOUT_DIR, 'parts', 'rubygems'),
    'RUBYLIB': os.environ.get('RUBYLIB', ''),
}
os.environ['GEM_HOME'] = '%(PREFIX)s/lib/ruby/gems/1.8' % s
os.environ['RUBYLIB'] = ':'.join([
    '%(RUBYLIB)s', '%(PREFIX)s/lib', '%(PREFIX)s/lib/ruby',
    '%(PREFIX)s/lib/site_ruby/1.8',]) % s


ugettext = lambda s: s

DEBUG = True
TEMPLATE_DEBUG = DEBUG
MEDIA_DEV_MODE = DEBUG
THUMBNAIL_DEBUG = DEBUG

ADMINS = (
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BUILDOUT_DIR, 'var', 'development.db'),
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'UTC'

LANGUAGES = (
    ('en', ugettext(u'English')),
)

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en'

LOCALE_PATHS = (
    os.path.join(PROJECT_DIR, 'locale'),
)

SITE_ID = 1

# Django-registration settings.
ACCOUNT_ACTIVATION_DAYS = 7

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(BUILDOUT_DIR, 'var', 'www', 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

DEV_MEDIA_URL = '/static/'
PRODUCTION_MEDIA_URL = '/static/'

GENERATED_MEDIA_DIR = os.path.join(BUILDOUT_DIR, 'var', 'www', 'static')
IMPORTED_SASS_FRAMEWORKS_DIR = os.path.join(BUILDOUT_DIR, 'var',
                                            'sass-frameworks')

GLOBAL_MEDIA_DIRS = (
    os.path.join(PROJECT_DIR, 'static'),
    os.path.join(BUILDOUT_DIR, 'parts', 'modernizr'),
    os.path.join(BUILDOUT_DIR, 'parts', 'jquery'),
    IMPORTED_SASS_FRAMEWORKS_DIR,
)

MEDIA_BUNDLES = (
    ('screen.css',
        'css/screen.sass',
    ),
    ('modernizr.js',
        'js/modernizr.js',
    ),
    ('scripts.js',
        'js/jquery.js',
        'js/plugins.js',
        'js/scripts.js',
    ),
)

SASS_FRAMEWORKS = (
    'compass',
)

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
ADMIN_MEDIA_PREFIX = '/static/admin/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '8m86q=ycpwma&n1f0t-l)y(i&lx*aon=%!(uuv985a-t+a_bfw'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'mediagenerator.middleware.MediaMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.transaction.TransactionMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

ROOT_URLCONF = 'project.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_DIR, 'templates'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    'project.context_processors.settings_for_context',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.markup',
    'south',
    'mediagenerator',
    'sorl.thumbnail',

    'debug_toolbar',
    'django_extensions',
    'test_utils',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

INTERNAL_IPS = (
    '127.0.0.1',
)

EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = os.path.join(BUILDOUT_DIR, 'var', 'mail')

CACHE_BACKEND = "dummy://"

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
}

DEFAULT_FROM_EMAIL = 'sirex@sirex-thinkpad'
JQUERY_VERSION = '1.7'
