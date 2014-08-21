"""The base url config file for the project."""

from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    '',
    url(r'^blog/', include('blog.urls', namespace='blog')),
    url(r'^contactme/', include('contactme.urls', namespace='contactme')),
    url(r'^', include('index.urls', namespace='index'))
)
