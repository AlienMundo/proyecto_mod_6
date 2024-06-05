from django.urls import path
from main.views import indice, acerca, bienvenido

urlpatterns = [
    path('', indice),
    path('acerca/', acerca),
    path('bienvenido/', bienvenido)
]