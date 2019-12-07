from django.shortcuts import render
from django.http import HttpResponse, Http404

from users.forms import CustomUserCreationForm
from users.templates.users.dictionnary import DICTIO

def create_user(request):
    """ This function will be used to display a template for user creation"""
    try:
        form = CustomUserCreationForm()
        DICTIO["form"] = form
        return render(request, "users/ess_remp.html",
                      DICTIO,
                     )
    except:
        raise Http404("Page not found")

def modify_user(request):
    """ This function will display a template for user modification"""
    try:
        return HttpResponse("Page not done yet")
    except:
        raise Http404("Page not found")

def delete_user(request):
    """ This function will display a template for user deletion"""
    try:
        return HttpResponse("Page not done yet")
    except:
        raise Http404("Page not found")
