from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import admin

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/(.*)', admin.site.root),
)

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
