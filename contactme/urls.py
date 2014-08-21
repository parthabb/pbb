"""The base url config file for the contactme app."""

__author__ = 'Partha Baruah (parthabb@gmail.com)'

from django.conf.urls import patterns, url


urlpatterns = patterns(
    'contactme.views',
    url(r'$', 'index', name='index')
)
