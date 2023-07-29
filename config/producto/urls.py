from django.contrib.auth import logout
from django.urls import path

from .views import listar_productos, crear_producto, editar_producto, iniciar_sesion, eliminar, buscar, registro, \
    cerrar_sesion

urlpatterns = [
    path('listar_productos/', listar_productos, name='listar_productos'),
    path('crear_producto/', crear_producto, name='crear_producto'),
    path('editar_producto/<int:producto_id>', editar_producto, name='editar_producto'),
    path('logout/', cerrar_sesion, name='logout'),
    path('login/', iniciar_sesion, name='login'),
    path('registrar/', registro, name='registrar'),
    path('eliminar/<int:producto_id>', eliminar, name='eliminar'),
    path('buscar/', buscar, name='buscar'),
]
