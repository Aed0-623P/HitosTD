"""
URL configuration for onlyflans project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from web.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", all_productos_view, name="index"),  
    path("about/", about, name="about"),
    path("contacto/", contacto, name="contacto"),
    path("exito/", exito, name="exito"),
    path('registration/', include('django.contrib.auth.urls')),
    path('producto/<int:producto_id>/', prod_detail, name='prod_detail'),
    path('producto/search/', prod_search, name='prod_search'),
    
    # Detail views for each product type
    path('pasta/<int:producto_id>/', pasta_detail_view, name='pasta_detail'),
    path('salsa/<int:producto_id>/', salsa_detail_view, name='salsa_detail'),
    path('dulce/<int:producto_id>/', dulce_detail_view, name='dulce_detail'),
    path('coctel/<int:producto_id>/', coctel_detail_view, name='coctel_detail'),
    
    # List views for each product type
    path('pasta/', list_all_pasta_view, name='list_all_pasta'),
    path('salsa/', list_all_salsa_view, name='list_all_salsa'),
    path('dulce/', list_all_dulce_view, name='list_all_dulce'),
    path('coctel/', list_all_coctel_view, name='list_all_coctel'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
