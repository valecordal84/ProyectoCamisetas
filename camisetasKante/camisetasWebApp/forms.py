from django import forms

class InventarioForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    tipo = forms.CharField(max_length=50, required=True)
    precio=forms.IntegerField(required=True)
    
class ClienteForm(forms.Form):
    nombreComprador = forms.CharField(max_length=50, required=True)
    mailComprador = forms.EmailField(max_length=50, required=True)
    direccionComprador= forms.CharField(required=True)
    telefono=forms.IntegerField(required=True)
    
class PedidoForm(forms.Form):
    nombreComprador = forms.CharField(max_length=50, required=True)
    direccionComprador= forms.CharField(max_length=50, required=True)
    precio=forms.IntegerField(required=True)