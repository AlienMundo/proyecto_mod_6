from django.shortcuts import render
from django.http import HttpResponse
from main.flanes import flanes

# Create your views here.

def indice(req):
    context = {'flanes': flanes}
    return render(req, 'indice.html', context)
