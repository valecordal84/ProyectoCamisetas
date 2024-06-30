from django.contrib import admin
from .models import Pedido, Cliente, Inventario
# Register your models here.

class PedidoAdmin(admin.ModelAdmin):
    readonly_fields=('horaPedido',)
    
class InventarioAdmin(admin.ModelAdmin):
    readonly_fields=('arribo',)
    
admin.site.register(Pedido, PedidoAdmin)
admin.site.register(Inventario, InventarioAdmin)
admin.site.register(Cliente)