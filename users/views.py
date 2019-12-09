from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.contrib.auth import login, authenticate

from users.forms import CustomUserCreationForm, ConnexionForm
from users.templates.users.dictionnary import DICTIO

def create_user(request):
    """ This function will be used to display a template for user creation"""
    try:
        if request.method == 'POST':
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                login(request, user)

                # For now, redirects to dbproducts (change later)
                return redirect('index')
            else:
                DICTIO["form"] = form

        else:
            form = CustomUserCreationForm()
            DICTIO["form"] = form
        return render(request, "users/create_user.html",
                      DICTIO,
                     )
    except:
        raise Http404("Page not found")

def log_in(request):
    """ This function will display a template for user identification"""
    DICTIO["error"] = False
    try:
        if request.method == "POST":
            form = ConnexionForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data["username"]
                password = form.cleaned_data["password"]
                user = authenticate(username=username, password=password)
                if user:
                    login(request, user)
                    # For now, redirects to dbproducts (change later)
                    return redirect("index")
                else:
                    DICTIO["error"] = True
        else:
            form = ConnexionForm()
            DICTIO["form"] = form

        return render(request, 'users/login.html', DICTIO)

    except:
        raise Http404("Page not found")

def delete_user(request):
    """ This function will display a template for user deletion"""
    try:
        return HttpResponse("Page not done yet")
    except:
        raise Http404("Page not found")
