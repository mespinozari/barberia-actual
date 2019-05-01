from django.contrib import admin
from .models import Barbero,Cliente,Servicio,Reserva

admin.site.register(Barbero)
admin.site.register(Cliente)
admin.site.register(Servicio)
admin.site.register(Reserva)

# Register your models here.
