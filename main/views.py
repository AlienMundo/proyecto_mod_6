from django.shortcuts import render
from django.http import HttpResponse
from main.flanes import flanes

# Create your views here.

def indice(req):
    context = {'flanes': flanes}
    return render(req, 'indice.html', context)

def acerca(req):
    context = {'titulo': 'Acerca de nosotros'}
    return render(req, 'acerca.html', context)

def bienvenido(req):
    return render(req, 'bienvenido.html')