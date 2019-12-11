from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.contrib.auth import login, authenticate, update_session_auth_hash, logout
from django.contrib import messages

from users.forms import CustomUserCreationForm, ConnexionForm, CustomUserChangeForm, CustomUserChangePassword
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

def disconnect_user(request):
    logout(request)
    return redirect("index")

def edit_profile(request):
    """ This function will display a template for user deletion"""
    try:
        if "passw" in request.POST:
            return redirect("change_password")

        if request.method == "POST" and "confirm" in request.POST:
            form = CustomUserChangeForm(request.POST, instance=request.user)

            if form.is_valid():
                form.save()
                # For now, redirects to dbproducts (change later)
                return redirect("index")
        else:
            form = CustomUserChangeForm(instance=request.user)
            DICTIO["form"] = form
        return render(request,
                      "users/edit_profile.html",
                      DICTIO,
                     )
    except:
        raise Http404("Page not found")

def change_password(request):

    try:
        if request.method == "POST":
            form = CustomUserChangePassword(request.user, request.POST)

            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request, user)
                messages.success(request, "Your password was successfully updated!")
                return redirect ("change_password")
            else:
                messages.error(request, "Please correct the error below")
        else:
            form = CustomUserChangePassword(request.user)
            DICTIO["form"] = form
        return render(request,
                      'users/change_password.html',
                      DICTIO,
                     )
    except:
        raise Http404("Page not found")
