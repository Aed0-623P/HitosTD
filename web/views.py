from django.shortcuts import render, redirect
from .models import Flan
from .forms import ContactFormForm

# Create your views here.

def index(request):
    flanes_publicos = Flan.objects.filter(is_private = False)
    return render(request, 'index.html', {'flanes': flanes_publicos})

def about(request):
    return render(request, 'about.html')

def exito(request):
    return render(request, 'exito.html')

def welcome(request):
    flanes_privados = Flan.objects.filter(is_private=True)
    return render(request, 'welcome.html', {'flanes' : flanes_privados})

def test(request):
    return render(request, 'test.html')

def contacto(request):
    if request.method == 'POST':
        form = ContactFormForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('exito')
    else:
        form = ContactFormForm()
    return render(request, 'contacto.html', {'form': form})