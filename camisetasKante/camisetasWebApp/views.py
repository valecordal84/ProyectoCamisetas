from django.shortcuts import render, HttpResponse
from .forms import *
from .models import *
# Create your views here.

def home(request):
    return render(request, "camisetasWebApp/home.html")

def camisetas(request):
    return render(request, "camisetasWebApp/camisetas.html")

def conjuntos(request):
    return render(request, "camisetasWebApp/conjuntos.html")

def accesorios(request):
    return render(request, "camisetasWebApp/accesorios.html")

def contacto(request):
    return render(request, "camisetasWebApp/contacto.html")

def agregarInventario(request):
    if request.method == "POST":
        miForm=InventarioForm(request.POST)
        if miForm.is_valid():
            inventario_nombre=miForm.cleaned_data.get("nombre")
            inventario_tipo=miForm.cleaned_data.get("tipo")
            inventario_precio=miForm.cleaned_data.get("precio")
            inventario= Inventario(nombre=inventario_nombre, tipo=inventario_tipo, precio=inventario_precio)
            inventario.save()
            return render(request, "camisetasWebApp/home.html")
            
    else:
        miForm=InventarioForm()
    
    return render(request, "camisetasWebApp/inventarioForm.html", {"form" : miForm})

def agregarCliente(request):
    if request.method == "POST":
        miForm=ClienteForm(request.POST)
        if miForm.is_valid():
            cliente_nombre=miForm.cleaned_data.get("nombreComprador")
            cliente_direccion=miForm.cleaned_data.get("direccionComprador")
            cliente_mail=miForm.cleaned_data.get("mailComprador")
            cliente_telefono=miForm.cleaned_data.get("telefono")
            cliente=Cliente(nombreComprador=cliente_nombre, mailComprador=cliente_mail, direccionComprador=cliente_direccion, telefono=cliente_telefono)
            cliente.save()
            return render(request, "camisetasWebApp/home.html")
    else:
        miForm=ClienteForm()
    return render(request, "camisetasWebApp/clienteForm.html", {"form": miForm})

def agregarPedido(request):
    if request.method == "POST":
        miForm=PedidoForm(request.POST)
        if miForm.is_valid():
            pedido_nombre=miForm.cleaned_data.get("nombreComprador")
            pedido_direccion=miForm.cleaned_data.get("direccionComprador")
            pedido_precio=miForm.cleaned_data.get("precio")
            pedido=Pedido(nombreComprador=pedido_nombre, direccionComprador=pedido_direccion, precio=pedido_precio)
            pedido.save()
            return render(request, "camisetasWebApp/home.html")
    else:
        miForm=ClienteForm()
    return render(request, "camisetasWebApp/pedidoForm.html", {"form" : miForm})
            
            
def buscarInventario(request):
    return render(request, "camisetasWebApp/buscarInventario.html")

def encontrarInventario(request):
    if request.GET["buscar"]:
        patron=request.GET["buscar"]
        inventario=Inventario.objects.filter(nombre__icontains=patron)
        contexto={'camisetas' : inventario}
    else:
        contexto={'camisetas' : Inventario.objects.all()}
        
    return render(request, "camisetasWebApp/camisetas.html", contexto)