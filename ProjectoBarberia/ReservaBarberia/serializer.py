from rest_framework import serializers,viewsets
from ReservaBarberia.models import Barbero

class BarberoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Barbero
        fields = ('barberonom','fecharegistro','descripcion','correo')

