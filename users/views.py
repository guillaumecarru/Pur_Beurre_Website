from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index_user(request):
    return render(request, "users/create_user.html", {
        "log" : {"welcome" : "Bienvenue, veuillez entrer vos informations de \
                 compte"}, \
        "guillaume":"openclassrooms" })
