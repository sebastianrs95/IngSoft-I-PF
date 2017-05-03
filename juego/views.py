from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Ahora crea y carga un template en juego.views")
