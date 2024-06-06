from django import forms
from .models import Cliente, Instalacion

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido', 'direccion', 'telefono', 'correo']

class InstalacionForm(forms.ModelForm):
    class Meta:
        model = Instalacion
        fields = ['cliente', 'tipo_fibra', 'router_bicanal', 'extensor_wifi', 'fecha_instalacion', 'hora_instalacion', 'comentario_adicional']
