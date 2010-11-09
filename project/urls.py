from django.conf.urls.defaults import patterns, handler500
from django.contrib import admin

admin.autodiscover()
handler500 # Pyflakes

urlpatterns = patterns('',
    (r'^admin/(.*)', admin.site.root),
)
