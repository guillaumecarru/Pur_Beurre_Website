from django.shortcuts import render

def homepage(request):
    """This function will display the main.html template, will render the
    homepage for this website"""
    DICTIO = {
        "title":"Du gras, oui, mais de qualité",
        "help_substitute":"Trouvez un produit de substitution pour ceux que \
vous consommez tous les jours.",
        "name":"Colette et Remy",
        "history":"Histoire à apposer",
        "contact":"Contactez-nous!",
    }

    return render(request, 'main/main.html', DICTIO)
