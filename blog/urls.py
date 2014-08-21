"""The base url config file for the blog app."""

__author__ = 'Partha Baruah (parthabb@gmail.com)'

from django.conf.urls import patterns, url


urlpatterns = patterns(
    'blog.views',
    url(r'$', 'index', name='index')
)
