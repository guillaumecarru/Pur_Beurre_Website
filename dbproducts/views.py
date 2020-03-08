from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.contrib.auth import logout
from django.contrib import messages
from django.utils.datastructures import MultiValueDictKeyError
from django.core.exceptions import ObjectDoesNotExist
from dbproducts.models import Product

# Index should be removed when main app will be added.
def index(request):
    if "disco" in request.POST:
        messages.success(request, "You are disconnected")
        logout(request)
    return render(request, "products/brief_index.html")

def research_substitute(request):
    DICTIO = {
        "research_title":"Résultats de recherche",
        "title":"Résultats de la recherche pour : ",
        "name":"Vous pouvez remplacer cet aliment par",
        "no_result":"Désolé, il n'y a pas de résultats pour ce produit",
        "link_text":"Lien vers la page du produit",
        "add_fav":"sauvegarder",
    }
    try:
        if request.GET["product"]:
            try:
                # Adding current product to DICTIO
                info_old_prod = Product.objects.get(product_name=request.GET["product"])
                DICTIO["old_prod"] = info_old_prod

                # Adding substitutes to DICTIO
                DICTIO["results"] = Product.objects.substitute(info_old_prod.product_name)

                # Returns new html page, with substitutes condensed information
                return render(request, "products/result_research.html", DICTIO)
            except ObjectDoesNotExist:
                # For now, redirects to Dbproducts; redirects somewhere else
                # later on
                messages.error(request, "Vous avez entré un produit non répertorié")
                return redirect("homepage")
    except MultiValueDictKeyError:
        return render(request, "main/main.html")

def detail(request, product_id):
    """ product_id is given from dbproducts/urls.py
    kwargs is given from template/products/result_research.py
    kwargs is here used to give old product info """
    DICTIO = {
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
    DICTIO["nutri_score"] = str(chr(info_prod.nutri_grade))
    DICTIO["info"] = info_prod
    return render(request, "products/show_product.html", DICTIO)
