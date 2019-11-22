from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index_user(request):
    return(HttpResponse("Will display something soon")
