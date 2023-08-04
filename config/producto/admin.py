from django.contrib import admin
from django.contrib.auth import logout
from .models import Producto, Fabrica


class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'precio', 'costo', 'descripcion', 'fecha_vencimiento', 'fabrica')
    list_filter = ('nombre', 'fabrica')
    list_display_links = ['id', 'nombre']
    list_per_page = 5
    # list_editable = ('nombre', 'precio', 'descripcion')
    search_fields = ['id', 'nombre', 'precio', 'descripcion', 'fecha_vencimiento']
    ordering = ['id']
    readonly_fields = ['fecha_vencimiento']

    def costo(self, obj):
        if obj.precio >= 2500:
            return 'Alto'
        elif obj.precio >= 1500:
            return 'Medio'
        else:
            return 'Bajo'


class FabricaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'pais')


# Register your models here.
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Fabrica, FabricaAdmin)

# admin.site.site_header = 'Catalogo de Productos'
# admin.site.index_title = 'Panel de control'
# admin.site.site_title = 'Panel de Control'
