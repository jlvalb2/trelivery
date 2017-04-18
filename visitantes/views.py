from django.shortcuts import render

# Create your views here.


def unica(request, plantilla):
    return render(request, plantilla)


def buscaRestaurantes(request, plantilla):
    return render(request, plantilla)


def restaurantesPorCEP(request, cep, plantilla):
    return render(request, plantilla)


def restaurantesPorMunicipio(request, municipio, plantilla):
    return render(request, plantilla)


def muestraCarta(request, restaurante, plantilla):
    return render(request, plantilla)
