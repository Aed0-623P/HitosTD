from django.shortcuts import get_object_or_404, render, redirect
from .models import *
from django.contrib.auth import login, authenticate
from .forms import ContactFormForm, SearchForm, RegistroUsuarioForm, CustomUserChangeForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from cart.cart import Cart
from django.contrib import messages
from cart import context_processors
import random



def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def politica(request):
    return render(request, 'politica.html')

def tyc(request):
    return render(request, 'tyc.html')

#contacto directo a un correo

def contacto(request):
    if request.method == 'POST':
        form = ContactFormForm(request.POST)
        if form.is_valid():
            instance = form.save()
            sender_email = instance.customer_email
            subject = instance.customer_name
            message = instance.message
            #send_mail(subject, message, settings.EMAIL_HOST_USER, [sender_email, 'test@mail.com'], fail_silently=False)  # Ensure 'to' is a list or tuple
            return redirect('exito')
    else:
        form = ContactFormForm()
    return render(request, 'contacto.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'

class CustomLogoutView(LogoutView):
    next_page = 'index.html'

#lista y detalle productos

def all_productos_view(request):
    all_products = Producto.objects.all()
    context = {
        'productos': all_products
    }
    return render(request, 'index.html', context)

def prod_detail(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    random_prod = random.sample(list(Producto.objects.exclude(pk=producto_id)), 3)
    context = {
        'producto': producto,
        'random_prod': random_prod,
        'user': request.user,
    }
    return render(request, 'detalle/prod_detail.html', context)

def list_all_pasta_view(request):
    all_pastas = Pasta.objects.all()
    context = {
        'pastas': all_pastas,
    }
    return render(request, 'listado/list_pasta.html', context)

def pasta_detail_view(request, producto_id):
    pasta_instance = get_object_or_404(Pasta, pk=producto_id)
    random_prod = random.sample(list(Pasta.objects.exclude(pk=producto_id)), 3)
    context = {
        'pasta': pasta_instance,
        'random_prod': random_prod,
    }
    return render(request, 'detalle/pasta_detail.html', context)

def list_all_salsa_view(request):
    all_salsa = Salsa.objects.all()
    context = {
        'salsas': all_salsa,
    }
    return render(request, 'listado/list_salsa.html', context)

def salsa_detail_view(request, producto_id):
    salsa_instance = get_object_or_404(Salsa, pk=producto_id)
    random_prod = random.sample(list(Pasta.objects.exclude(pk=producto_id)), 3)
    context = {
        'salsa': salsa_instance,
        'random_prod': random_prod,
    }
    return render(request, 'detalle/salsa_detail.html', context)

def list_all_dulce_view(request):
    all_dulce = Dulce.objects.all()
    context = {
        'dulces': all_dulce,
    }
    return render(request, 'listado/list_dulce.html', context)

def dulce_detail_view(request, producto_id):
    dulce_instance = get_object_or_404(Dulce, pk=producto_id)
    random_prod = random.sample(list(Pasta.objects.exclude(pk=producto_id)), 3)
    context = {
        'dulce': dulce_instance,
        'random_prod': random_prod,
    }
    return render(request, 'detalle/dulce_detail.html', context)

def list_all_coctel_view(request):
    all_coctel = Coctel.objects.all()
    context = {
        'coctel': all_coctel,
    }
    return render(request, 'listado/list_coctel.html', context)

def coctel_detail_view(request, producto_id):
    coctel_instance = get_object_or_404(Coctel, pk=producto_id)
    random_prod = random.sample(list(Pasta.objects.exclude(pk=producto_id)), 3)
    context = {
        'coctel': coctel_instance,
        'random_prod': random_prod,
    }
    return render(request, 'detalle/coctel_detail.html', context)

#search bar

def search_view(request):
    form = SearchForm(request.GET)
    results = []
    if form.is_valid():
        query = form.cleaned_data['query']
        results = Producto.objects.filter(name__icontains=query)
    return render(request, 'busqueda.html', {'results': results})

#carrito de compras

@login_required()
def cart_add(request, id):
    cart = Cart(request)
    product = Producto.objects.get(id=id)
    cart.add(product=product)
    return redirect("index")


@login_required()
def item_clear(request, id):
    cart = Cart(request)
    product = Producto.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required()
def item_increment(request, id):
    cart = Cart(request)
    product = Producto.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required()
def item_decrement(request, id):
    cart = Cart(request)
    product = Producto.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required()
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required()
def cart_detail(request):
    cart = Cart(request)
    return render(request, 'detalle/cart_detail.html', {'cart': cart.cart})

def registro_usuario(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            password = form.cleaned_data['password']
            usuario.set_password(password)
            usuario.save()
            # Autenticar al usuario después del registro
            usuario_autenticado = authenticate(username=usuario.username, password=password)
            if usuario_autenticado is not None:
                login(request, usuario_autenticado)
                return redirect('index')  
    else:
        form = RegistroUsuarioForm()
    return render(request, 'registro_usuario.html', {'form': form})

@login_required
def actualizar_usuario(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user.usuario)
        print(form)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Los datos del usuario han sido actualizados!')
            return redirect('index') 
    else:
        form = CustomUserChangeForm(instance=request.user.usuario)
    return render(request, 'perfil.html', {'form': form})

@login_required
def welcome(request):
    natalina_privados = Usuario.objects.filter()
    return render(request, 'welcome.html', {'natalina' : natalina_privados})

def exito(request):
    return render(request, 'exito.html')

#test area