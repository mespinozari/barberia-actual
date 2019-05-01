"""ProjectoBarberia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from ReservaBarberia import views
from django.contrib.auth.views import LoginView
from django.conf.urls import url,include
from rest_framework import routers
from ReservaBarberia.views import RegistrarBarbero

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('codigo/django',views.ejemplo,name='ejemplo'),
    path('inicio/',views.index,name='index'),
    path('nuevo/',views.reserva_view,name='reserva_view'),
    path('listar/',views.reserva_list,name='reserva_list'),
    path('editar/<codres>/',views.reserva_edit,name='reserva_edit'),
    path('eliminar/<codres>/',views.reserva_delete,name='reserva_delete'),
    path('login/',LoginView.as_view(template_name='login.html'),name='login'),
    path('listado/',views.reservas_json,name='listado'),
    path('barberos/',include('ReservaBarberia.urls')),
    path('registrobarbero/',RegistrarBarbero.as_view(),name='registrar_barbero')
    
]
