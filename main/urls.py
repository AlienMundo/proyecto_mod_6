from django.urls import path
from main.views import failure, index, about, success, welcome, contact_form, contact

urlpatterns = [
    path('', index),
    path('acerca/', about),
    path('contacto/', contact),
    path('bienvenido/', welcome),
    path('contact_form', contact_form),
    path('success/', success)
]