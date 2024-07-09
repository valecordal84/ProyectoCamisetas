from django import forms
from .models import Inventario

class InventarioForm(forms.Form):
    class Meta:
        model = Inventario
        fields=['nombre', 'precio']
    
class ClienteForm(forms.Form):
    nombre = forms.CharField(max_length=255, required=True)
    mail = forms.EmailField(max_length=255, required=True)
    direccion = forms.CharField(required=True)
    telefono = forms.IntegerField(required=True)
    
class PedidoForm(forms.Form):
    nombre = forms.CharField(max_length=255, required=True)
    direccion = forms.CharField(max_length=255, required=True)
    precio=forms.IntegerField(required=True)