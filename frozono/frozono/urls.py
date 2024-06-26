"""
URL configuration for frozono project.

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
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls), # Ruta para la administración de Django
    path('', views.home, name='home'), # Ruta para la página de inicio
    path('app/contacto.html', views.contacto, name='contacto'), # Ruta para la página de contacto
    path('app/catalogo.html', views.catalogo, name='catalogo'), # Ruta para la página de catalogo
    path('app/login.html', views.login, name='login'), # Ruta para la página de login
    path('app/productdetail.html', views.productdetail, name='productdetail'), # Ruta para la página de productdetail
    path('app/registro.html', views.registro, name='registro'), # Ruta para la página de productdetail
    path('app/aboutus.html', views.aboutus, name='aboutus'), #Ruta para la página Nosotres

]


