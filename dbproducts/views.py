from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.contrib.auth import logout
from django.contrib import messages

from .forms import ResearchProduct
from dbproducts.models import *

# Index should be removed when main app will be added.
def index(request):
    if "disco" in request.POST:
        messages.success(request, "You are disconnected")
        logout(request)
    return render(request, "products/brief_index.html")

def research_substitute(request):
    formes = {}
    if request.method == "POST":
        form = ResearchProduct(request.POST)
        formes["form"] = form
    return render(request, "products/research_bar.html", formes)

def detail(request, product_id):
    DICTIO = {
        # Dictionnary file_info is meant for show_product.html page
        "prod_info_var":{
            "prod_title":"Informations du produit",
            "specs":{
                "name":"Nom du produit",
                "nutri_score":"informations nutritionnelles",
                "web":"site web",
            },
            "link_name":"lien vers OpenFoodFacts",
        }
    }
    info_prod = Product.objects.get(id=product_id)
    DICTIO["info"] = info_prod
    return render(request, "products/show_product.html", DICTIO)
