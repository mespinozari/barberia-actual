from django import forms
from ReservaBarberia.models import Reserva

class ReservaForm (forms.ModelForm):
    class Meta:
        model = Reserva

        fields = [
            'codbarbero',
            'codclie',
            'codserv',
            'fecha',
            'obs'
        ]
        
        labels = {
            'codbarbero':'Barbero',
            'codclie':'Cliente',
            'codserv':'Servicio',
            'fecha':'Fecha_Reserva',
            'obs':'Obs',
        }

        widgets = {
            'codbarbero':forms.Select(attrs={'class':'form-control'}),
            'codclie':forms.Select(attrs={'class':'form-control'}),
            'codserv':forms.CheckboxSelectMultiple(),
            'fecha':forms.TextInput(attrs={'class':'form-control'}),
            'obs':forms.Textarea(attrs={'class':'form-control'}),
        } 

