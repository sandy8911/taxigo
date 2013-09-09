#encoding:utf-8
from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
#Descubre las secciones instaladas en nuestro proyecto
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'choferes.views.inicio', name='inicio'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
