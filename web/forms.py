import django.forms
from .models import ContactForm, Usuario
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm


class ContactFormForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ['customer_email', 'customer_name', 'message']
        labels = {
            'customer_email': 'Correo electrónico',
            'customer_name': 'Nombre',
            'message': 'Mensaje'}
        
class SearchForm(forms.Form):
    query = forms.CharField(label='buscar')

class RegistroUsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['username', 'password', 'nombre', 'apellido', 'rut', 'direccion', 'telefono', 'correo_electronico']
        widgets = {
            'password': forms.PasswordInput(),
        }

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User
        fields = ['first_name', 'last_name', 'email']