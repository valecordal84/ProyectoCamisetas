from django.db import models

# Create your models here.

class Pedido(models.Model):
    nombre=models.CharField(max_length=255)
    direccion=models.CharField(max_length=255)
    productos=models.CharField(max_length=255)
    precio=models.IntegerField()
    horaPedido=models.DateTimeField(auto_now_add=True)
    
class Cliente(models.Model):
    nombre=models.CharField(max_length=255)
    mail=models.EmailField()
    direccion=models.CharField(max_length=255)
    telefono=models.IntegerField()
    
class Inventario(models.Model):
    nombre=models.CharField(max_length=255)
    precio=models.IntegerField()
    arribo=models.DateTimeField(auto_now_add=True)