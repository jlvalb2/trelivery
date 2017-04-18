from django.shortcuts import render

# Create your views here.


def unica(request, plantilla):
    return render(request, plantilla)
