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
from django.urls import path, include, re_path
from web.views import index,about,welcome,contacto,exito,flan_search
from web import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("",index,name="index"),
    path("about/",about,name="about"),
    path("welcome/",welcome,name="welcome"),
    path("contacto/", contacto,name="contacto"),
    path("exito/", exito,name="exito"),
    path('registration/', include('django.contrib.auth.urls')),
    path('flan/<int:flan_id>/', views.flan_detail, name='flan_detail'),
    re_path(r'^.*$', views.error_404),
    path('flan/search/', flan_search, name='flan_search'),
    ]