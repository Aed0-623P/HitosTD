from django.shortcuts import get_object_or_404, render, redirect
from .models import Flan
from .forms import ContactFormForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    flanes_publicos = Flan.objects.filter(is_private = False)
    return render(request, 'index.html', {'flanes': flanes_publicos})

def about(request):
    return render(request, 'about.html')

def exito(request):
    return render(request, 'exito.html')

def error_404(request):
    return render(request, '404.html', status=404)

@login_required
def welcome(request):
    flanes_privados = Flan.objects.filter(is_private=True)
    return render(request, 'welcome.html', {'flanes' : flanes_privados})

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

def flan_detail(request,flan_id):
    flan = get_object_or_404(Flan, pk=flan_id)
    return render(request, 'flan_detail.html', {'flan': flan})

