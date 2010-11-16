from django.conf import settings
from django.conf.urls.defaults import patterns, handler500
from django.contrib import admin

from staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()
handler500 # Pyflakes

urlpatterns = patterns('',
    (r'^admin/(.*)', admin.site.root),
)

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
