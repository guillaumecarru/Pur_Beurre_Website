from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from favorites.models import Favorites

@login_required(login_url='/users/log_in/')
def add_favorites(request, **kwargs):
    """ Redirected to this function, user will add the favorite to its list if
    he is connected"""
    # Should write favorites.urls to link with detail
    return 1
