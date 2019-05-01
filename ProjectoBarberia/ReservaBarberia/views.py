from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from ReservaBarberia.forms import ReservaForm
from ReservaBarberia.models import Reserva,Barbero
from django.core import serializers
from .serializer import BarberoSerializer
from rest_framework import viewsets

from django.template import RequestContext
from django.views.generic import CreateView
from django.urls import reverse_lazy

def home (request):
    context = {'foo': 'bar'}
    return render(request,'base.html',context)
    
def ejemplo(request):
    context = {'foo': 'bar'}
    titulo = 'Django vive en codigo'
    nombre = 'Pasando variables en Django'
    lista =[2,3,5,65,78,98,234,567,876]
    return render(request,'ejemplo.html',{'title':titulo,'nombre':nombre,'lista':lista},context)

def index (request):
    return render (request,'reservas/index.html')   

def reserva_view(request):
    if request.method == "POST":
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request,'reservas/index.html',{'form':form})
    else:
        form = ReservaForm()
    return render(request,'reservas/reserva_form.html',{'form':form})

def reserva_list (request):
    reserva = Reserva.objects.all()
    contexto = {'reservas': reserva}
    return render(request,'reservas/reserva_list.html',contexto)

def reserva_edit (request,codres):
    reserva= Reserva.objects.get(codreserva=codres)
    if request.method == 'GET':
        form = ReservaForm(instance=reserva)
    else:
        form = ReservaForm(request.POST,instance=reserva)
        if form.is_valid():
            form.save()
            reserva = Reserva.objects.all()
            contexto = {'reservas': reserva}
            return render(request,'reservas/reserva_list.html',contexto)
    return render (request,'reservas/reserva_form.html',{'form':form})      

def reserva_delete(request,codres):
    reserva= Reserva.objects.get(codreserva=codres)
    if request.method == 'POST' :
        reserva.delete()
        reserva = Reserva.objects.all()
        contexto = {'reservas': reserva}
        return render(request,'reservas/reserva_list.html',contexto)
    return render(request,'reservas/reserva_delete.html',{'reserva':reserva})    

def reservas_json(request):
    lista = serializers.serialize('json',Reserva.objects.all(),fields=['codbarbero','codclie'])    
    return HttpResponse(lista,content_type='application/json')

class BarberoList(viewsets.ModelViewSet):
    queryset = Barbero.objects.all()
    serializer_class=BarberoSerializer

class RegistrarBarbero(CreateView):
    template_name = 'barberos/barberos_registro.html'
    model = Barbero
    fields = ('barberonom','fecharegistro','descripcion')
    success_url=reverse_lazy ('barberos/barberos_registro.html')

    def post(self, request, *arg, **kwargs):
        estado =False
        barbero= Barbero()
        barbero.barberonom = request.POST['nombre']
        barbero.fecharegistro = request.POST['fecha']
        barbero.descripcion = request.POST['descripcion']
        barbero.save()
        estado =True
        dic = {'estado' : estado}
        contexto = {'barbero':barbero}
        return render(request,'barberos/barberos_registro.html',dic,contexto)












# Create your views here.
