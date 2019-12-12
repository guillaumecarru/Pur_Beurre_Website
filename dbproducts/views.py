from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import logout
from django.contrib import messages


from dbproducts.models import *
from dbproducts.templates.products.dictionnary import DICTIO

def index(request):
    if "disco" in request.POST:
        messages.success(request, "You are disconnected")
        logout(request)
    return render(request, "products/brief_index.html")

def research_substitute(request):
    return render(request, "products/research_bar.html")

def detail(request, product_id):
    info_prod = Product.objects.get(id=product_id)
    DICTIO["info"] = info_prod
    return render(request, "products/show_product.html", DICTIO)

