from django.contrib.auth import logout
from django.urls import path

from .views import listar_productos, crear_producto, editar_producto, iniciar_sesion, eliminar, buscar, registro, \
    cerrar_sesion, eliminar_confirmacion

urlpatterns = [
    path('listar_productos/', listar_productos, name='listar_productos'),
    path('crear_producto/', crear_producto, name='crear_producto'),
    path('editar_producto/<int:producto_id>', editar_producto, name='editar_producto'),
    # Paths para la eliminación de productos
    path('eliminar/<int:producto_id>', eliminar_confirmacion, name='eliminar_confirmacion'),
    path('confirmar/<int:producto_id>/', eliminar, name='eliminar'),
    path('logout/', cerrar_sesion, name='logout'),
    path('login/', iniciar_sesion, name='login'),
    path('registro/', registro, name='registro'),
    path('buscar/', buscar, name='buscar'),

]

