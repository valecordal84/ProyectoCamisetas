from django.db import models

# Create your models here.

class Inventario(models.Model):
    nombre=models.CharField(max_length=50)
    tipo=models.CharField(max_length=50)
    precio=models.IntegerField()
    arribo=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name="inventario"
        verbose_name_plural="inventarios"
    
    def __str__(self):
        return self.nombre
    

class Pedido(models.Model):
    nombreComprador=models.CharField(max_length=50)
    direccionComprador=models.CharField(max_length=50)
    precio=models.IntegerField()
    horaPedido=models.DateTimeField(auto_now_add=True)
    

class Cliente(models.Model):
    nombreComprador=models.CharField(max_length=50)
    mailComprador=models.EmailField()
    direccionComprador=models.CharField(max_length=50)
    telefono=models.IntegerField()