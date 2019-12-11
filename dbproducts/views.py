from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import logout
from django.contrib import messages

def index(request):
    if "disco" in request.POST:
        messages.success(request, "You are disconnected")
        logout(request)
    return render(request, "products/brief_index.html")
