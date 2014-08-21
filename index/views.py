"""Module to handle the different views to the index app"""

__author__ = 'Partha Baruah (parthabb@gmail.com)'


from django.shortcuts import render_to_response


# Create your views here.
def index(req):
    """Handles the index view."""
    data = {'page': 'index'}
    return render_to_response(
        'index/index.html',
        data)
