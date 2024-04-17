import django.forms
from .models import ContactForm
from django import forms


class ContactFormForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ['customer_email', 'customer_name', 'message']
        labels = {
            'customer_email': 'Correo electrónico',
            'customer_name': 'Nombre',
            'message': 'Mensaje'}
