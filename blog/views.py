"""Module to handle the different views to the blog app"""

__author__ = 'Partha Baruah (parthabb@gmail.com)'


from django.shortcuts import render_to_response


# Create your views here.
def index(req):
    """Handles the index view."""
    data = {'page': 'blog'}
    return render_to_response(
        'blog/index.html',
        data)
