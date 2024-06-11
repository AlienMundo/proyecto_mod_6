from django.urls import path
from main.views import failure, index, about, success, welcome, contact_form, contacto

urlpatterns = [
    path('', index),
    path('acerca/', about),
    path('contact/', contacto),
    path('bienvenido/', welcome),
    path('contact_form', contact_form),
    path('success/', success)
]