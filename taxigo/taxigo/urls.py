#encoding:utf-8
from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'choferes.views.inicio', name='inicio'),
    url(r'^addchofer/$','choferes.views.addChofer', name = 'addChofer'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
