"""The base url config file for the index app."""

__author__ = 'Partha Baruah (parthabb@gmail.com)'

from django.conf.urls import patterns, url


urlpatterns = patterns(
    'index.views',
    url(r'$', 'index', name='index')
)
