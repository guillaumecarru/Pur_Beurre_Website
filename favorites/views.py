from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate

from django.core.exceptions import ObjectDoesNotExist

from django.contrib import messages
from favorites.models import Favorites
from dbproducts.models import Product


@login_required(login_url='/users/log_in/')
def add_favorites(request):
    """ Redirected to this function, user will add the favorite to its list if
    he is connected"""
    DICTIO = {
        "error_msg":"Vous avez déjà ajouté ce produit aux favoris",
        "valid_add":"Produit ajouté",
        "title":"Ajout aux favoris",
        "err_product":"Ne marche pas",
    }
    if request.method == "POST":
        if "prev_prod" in request.POST:
            prev_product = Product.objects.get(id=int(request.POST["prev_prod"]))
            favorite = Product.objects.get(id=int(request.POST["new_sub"]))
            customer = request.user

            # Adding those informations to favorites
            adding = Favorites.objects.get_or_create(substitute=favorite,
                                                     original_prod=prev_product,
                                                     user=customer,
                                                    )
            if adding[1]:
                # Means object just been created
                messages.success(request, DICTIO["valid_add"])
            else:
                messages.error(request, DICTIO["error_msg"])
        else:
            messages.error(request, DICTIO["error_msg"])

        return render(request, "favorites/add_favorites.html", DICTIO)

@login_required(login_url='/users/log_in/')
def consult_favorites(request):
    """Allows user to consult his favorites"""
    DICTIO = {
        "title":"Page de favoris",
        "button_fav":"favoris",
        "no_product":"Vous n'avez pas encore de favoris",
        "infos":{
            "old_prod":"Produit substitué",
            "substitute":"Substitut",
        }
    }
    if request.method == "POST":
        current_user = request.user
        user_favorites = Favorites.objects.filter(user=current_user)
        DICTIO["favorites"] = user_favorites
        return render(request, "favorites/registered_favorites.html", DICTIO)
    return render(request, "favorites/button_favorites.html", DICTIO)
