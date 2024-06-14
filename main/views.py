from django import forms
from django.shortcuts import redirect, render
from django.http import HttpResponse
from main.flanes import flanes
from main.forms import ContactForm, RegisterForm
from main.models import Cliente, Flan

from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.

def index(req):
    # Debe mostrar todos los flanes de la base de datos
    flanes_publicos = Flan.objects.filter(is_private=False)
    context = {
        'flanes_publicos': flanes_publicos
    }
    return render(req, 'index.html', context)

def about(req):
    return render(req, 'about.html')

@login_required #Esto evita que puedan entrar a la pagina "welcome"sin haberse logeado antes
def welcome(req):
    # Debe mostrar solo los flanes privados de la base de datos
    flanes = Flan.objects.all()
    context = {
        'flanes': flanes
    }
    return render(req, 'welcome.html', context)

def contact(req):
    if req.method == 'GET':
        # Renderizamos la pagina
        form = ContactForm()
        context = {'form':form}
        return render(req, 'contacto.html', context)

    else:
        # validamos el formulario
        form = ContactForm(req.POST)
        if form.is_valid():
            Cliente.objects.create(
                # Esta es la forma de pedirle a un modelo que cree un registro usando los datos de un formulario
                **form.cleaned_data
            )
            return redirect('/success')
        context = {'form':form}
        return render(req, 'contacto.html', context)

def contact_form(req):
    customer_name = req.POST['customer_name']
    customer_email = req.POST['customer_email']
    message = req.POST['message']

    errores = []

    if "@" in customer_email and len(customer_name) <= 64:
        return redirect('/success')
    else:
        errores.append('Error en el envio, formato no valido')
        context = {'errores': errores}
        return render(req, 'welcome.html', context)
    
    # ahora tengo que validar  que 'customer_email' tenga al menos 1 arroba y que 'customer_name' sea de largo maximo 64 caracteres

    # Si se pilla algun error se agrega a errores, si len(errores) == 0: redirigimos a pagina de exito
    # Si len(errores) > 0: vuelvo a cargar 'welcome.html', pero ahora mostrando los errores


def success(req):
    return render(req, 'success.html')

def failure(req):
    return render(req, 'failure.html')

# Sobreescribimos la viesta del login
class LoginViewPropia(SuccessMessageMixin, LoginView):
    success_message = 'Has ingresado correctamente'

    


def logout(req):
    return render(req, 'logout.html')

def register(req):
    return render(req, 'register.html')

usuarios = []
def agregar_usuario(req):
    nuevo_usuario = req.POST['usuario']
    usuarios.append(nuevo_usuario)
    return redirect('/')


def register(req):
    form = RegisterForm()
    context = {'form': form}
    if req.method == 'GET':
        return render(req, 'registration/register.html', context)
    
    # En caso de post se manda de vuelta
    form = RegisterForm(req.POST)
    if form.is_valid():
        data = form.cleaned_data
        if data['password'] != data['password2']:
            messages.warning(req, 'La contraseña es diferente')
            return redirect('/accounts/register/')
        
        User.objects.create_user(data['username'], data['password'])
        messages.success(req, 'El usuario ha sido creado con exito.')
    return redirect('/')

