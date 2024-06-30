from django.shortcuts import render, HttpResponse

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

def busquedaInventario(request):
    return render (request, "camisetasWebApp/bsqinv.html")

def inventario(request):
    
    mensaje="El artículo buscado es: %r" %request.GET["producto"]
    
    return HttpResponse(mensaje)