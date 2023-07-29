from django.contrib import admin
from django.contrib.auth import logout
from .models import Producto, Fabrica


class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'precio', 'descripcion', 'fabrica')


class FabricaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')


# Register your models here.
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Fabrica, FabricaAdmin)
