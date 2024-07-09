from django.shortcuts import render, HttpResponse
from .forms import *
from .models import *

# Create your views here.

#Views principales
def home(request):
    return render(request, "webapp/home.html")

def contacto(request):
    return render(request, "webapp/contacto.html")

def inventario(request):
    return render(request, "webapp/inventario.html")


#Agregar
def agregarCliente(request):
    if request.method == "POST":
        miForm=ClienteForm(request.POST)
        if miForm.is_valid():
            cliente_nombre=miForm.cleaned_data.get("nombre")
            cliente_direccion=miForm.cleaned_data.get("direccion")
            cliente_mail=miForm.cleaned_data.get("mail")
            cliente_telefono=miForm.cleaned_data.get("telefono")
            cliente=Cliente(nombre=cliente_nombre, mail=cliente_mail, direccion=cliente_direccion, telefono=cliente_telefono)
            cliente.save()
            return render(request, "webapp/home.html")
    else:
        miForm=ClienteForm()
    return render(request, "webapp/clienteForm.html", {"form": miForm})

def agregarPedido(request):
    if request.method == "POST":
        miForm=PedidoForm(request.POST)
        if miForm.is_valid():
            pedido_nombre=miForm.cleaned_data.get("nombre")
            pedido_direccion=miForm.cleaned_data.get("direccion")
            pedido_precio=miForm.cleaned_data.get("precio")
            pedido=Pedido(nombre=pedido_nombre, direccion=pedido_direccion, precio=pedido_precio)
            pedido.save()
            return render(request, "webapp/home.html")
    else:
        miForm=ClienteForm()
    return render(request, "webapp/pedidoForm.html", {"form" : miForm})

def agregarInventario(request):
    if request.method == "POST":
        miForm=InventarioForm(request.POST)
        if miForm.is_valid():
            inventario_nombre=miForm.cleaned_data.get("nombre")
            inventario_precio=miForm.cleaned_data.get("precio")
            inventario=Inventario(nombre=inventario_nombre, precio=inventario_precio)
            inventario.save()
            return render(request, "webapp/inventario.html")
    else:
        miForm=ClienteForm()
    return render(request, "webapp/inventarioForm.html", {"form" : miForm})
            

#Busqueda
def buscarInventario(request):
    return render(request, "webapp/buscarInventario.html")

def encontrarInventario(request):
    if request.GET["buscar"]:
        patron=request.GET["buscar"]
        inventario=Inventario.objects.filter(nombre__icontains=patron)
        contexto={'camisetas' : inventario}
    else:
        contexto={'camisetas' : Inventario.objects.all()}
        
    return render(request, "webapp/inventario.html", contexto)