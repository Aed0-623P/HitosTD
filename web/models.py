from django.db import models
import uuid
from django.utils.text import slugify
from django.contrib.auth.models import User

# Create your models here.

class Producto(models.Model):
    producto_uuid = models.UUIDField(default= uuid.uuid4, editable= False, unique=True)
    name = models.CharField(max_length=64)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=0)
    image_url = models.ImageField(upload_to='',null=True, blank=True)
    slug = models.SlugField(unique=True, blank=True)
    is_private = models.BooleanField(default=False)

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args,**kwargs)

    def __str__(self):
        return self.name
    
class Pasta(Producto):
    tipo_pasta = models.CharField(max_length=100)

class Salsa(Producto):
    tipo_salsa = models.CharField(max_length=100)

class Dulce(Producto):
    tipo_dulce = models.CharField(max_length=100)

class Coctel(Producto):
    tipo_coctel = models.CharField(max_length=100)


    
class ContactForm(models.Model):
    contact_form_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    customer_email = models.EmailField()
    customer_name = models.CharField(max_length=64)
    message = models.TextField()

    def __str__(self):
        return self.customer_name