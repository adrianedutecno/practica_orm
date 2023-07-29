from django.contrib import messages
from django.contrib.auth import logout
from django.db.models import Q

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

from django.contrib.auth import authenticate, login

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from .forms import ProductoForm
from .models import Producto


# Create your views here.

# views o controlador para listar
def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'listar_productos.html', {'productos': productos})


# views o controlador para crear productos
def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)  # se captura el formulario
        if form.is_valid():  # se valida el formulario
            form.save()  # se guarda el formulario si es valido
            messages.success(request, 'Producto agregado correctamente')
            return redirect('listar_productos')
        else:
            messages.error(request, 'Datos inválidos para agregar el producto')
            return HttpResponseRedirect(reverse('crear_producto'))
    else:
        form = ProductoForm()
    return render(request, 'crear_producto.html', {'form': form})


# views o controlador para editar productos
def editar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)  # se captura el formulario
        if form.is_valid():  # se valida el formulario
            form.save()  # se guarda el formulario si es valido
            messages.success(request, 'Producto editado correctamente')
            return redirect('listar_productos')
        else:
            messages.error(request, 'Datos inválidos para editar el producto')
            return HttpResponseRedirect(reverse('editar_producto', args=[producto.id]))
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'editar_producto.html', {'form': form, 'producto_id': producto.id})



# views o controlador para cerrar_sesion
def cerrar_sesion(request):
    logout(request)
    return render(request, 'login.html')


def buscar(request):
    if request.method == 'GET':
        query = request.GET.get('query')  # obteniendo lo que trae el get
        productos = Producto.objects.filter(Q(nombre__icontains=query) | Q(fabrica__icontains=query))
        return render(request, 'buscar.html', {'productos': productos})


def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registrado exitosamente')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registro.html', {'form': form})


def iniciar_sesion(request):
    if request.method == 'POST':  # si el request es de tipo post
        username = request.POST['username']  # captura username del request
        password = request.POST['password']  # captura password del request
        user = authenticate(request, username=username, password=password)  # se captura el usuario encontrado
        if user is not None:  # si el usuario autenticado no viene vacio, quiere decir es validas sus credenciales
            login(request, user)
            return redirect('listar_productos')
        else:
            messages.error(request, 'Usuario o password inválidas')
            return render(request, 'login.html')
    return render(request, 'login.html')  # tipo get


# View para eliminar productos
def eliminar(request, producto_id):
    if request.method == 'POST':
        producto = get_object_or_404(Producto, id=producto_id)
        producto.delete()
        messages.success(request, 'Producto eliminado exitosamente.')
        return redirect('listar_productos')
    else:
        return redirect('listar_productos')


# View para confirmar eliminación de producto
def eliminar_confirmacion(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    return render(request, 'confirmar.html', {'producto': producto})
