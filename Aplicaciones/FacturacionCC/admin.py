from django.contrib import admin
from .models import  Detalle, Platillo, Ingrediente, Receta, Cliente, Tipo, Provincia, Pedido
# Register your models here.
admin.site.register(Provincia)
admin.site.register(Tipo)
admin.site.register(Ingrediente)
admin.site.register(Cliente)
admin.site.register(Pedido)
admin.site.register(Platillo)
admin.site.register(Detalle)
admin.site.register(Receta)
