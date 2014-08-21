"""Module to handle the different views to the contactme app"""

__author__ = 'Partha Baruah (parthabb@gmail.com)'


from django.shortcuts import render_to_response


# Create your views here.
def index(req):
    """Handles the index view."""
    data = {'page': 'contactme'}
    return render_to_response(
        'contactme/index.html',
        data)
