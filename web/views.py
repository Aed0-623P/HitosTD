from django.shortcuts import get_object_or_404, render, redirect
from .models import *
from .forms import ContactFormForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
import random
# Create your views here.

def index(request):
    return render(request, 'index.html', {})

def about(request):
    return render(request, 'about.html')

def exito(request):
    return render(request, 'exito.html')

def contacto(request):
    if request.method == 'POST':
        form = ContactFormForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('exito')
    else:
        form = ContactFormForm()
    return render(request, 'contacto.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'

class CustomLogoutView(LogoutView):
    next_page = '/'

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
    return render(request, 'prod_detail.html', context)


def list_all_pasta_view(request):
    all_pastas = Pasta.objects.all()
    context = {
        'pastas': all_pastas,
    }
    return render(request, 'list_pasta.html', context)

def pasta_detail_view(request, producto_id):
    pasta_instance = get_object_or_404(Pasta, pk=producto_id)
    context = {
        'pasta': pasta_instance,
    }
    return render(request, 'pasta_detail.html', context)


def list_all_salsa_view(request):
    all_salsa = Salsa.objects.all()
    context = {
        'salsas': all_salsa,
    }
    return render(request, 'list_salsa.html', context)

def salsa_detail_view(request, producto_id):
    salsa_instance = get_object_or_404(Salsa, pk=producto_id)
    context = {
        'producto': salsa_instance,
    }
    return render(request, 'salsa_detail.html', context)

def list_all_dulce_view(request):
    all_dulce = Dulce.objects.all()
    context = {
        'dulces': all_dulce,
    }
    return render(request, 'list_dulce.html', context)

def dulce_detail_view(request, producto_id):
    dulce_instance = get_object_or_404(Dulce, pk=producto_id)
    context = {
        'producto': dulce_instance,
    }
    return render(request, 'dulce_detail.html', context)

def list_all_coctel_view(request):
    all_coctel = Coctel.objects.all()
    context = {
        'coctel': all_coctel,
    }
    return render(request, 'list_coctel.html', context)

def coctel_detail_view(request, producto_id):
    coctel_instance = get_object_or_404(Coctel, pk=producto_id)
    context = {
        'producto': coctel_instance,
    }
    return render(request, 'coctel_detail.html', context)




#test area

def prod_search(request):
    query = request.GET.get('query')
    prod = Producto.objects.filter(name__icontains=query) if query else Producto.objects.none()
    return render(request, 'base.html', {'prod': prod, 'query': query})
