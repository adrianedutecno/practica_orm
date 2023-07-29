from django.contrib.auth import logout
from django.urls import path

from .views import listar_productos, crear_producto, editar_producto

urlpatterns = [
    path('listar_productos/', listar_productos, name='listar_productos'),
    path('crear_producto/', crear_producto, name='crear_producto'),
    path('editar_producto/<int:producto_id>', editar_producto, name='editar_producto'),
    path('logout/', cerrar_sesion ,name= 'logout'),
]
