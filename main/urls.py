from django.urls import path
from main.views import indice

urlpatterns = [
    path('', indice),
]