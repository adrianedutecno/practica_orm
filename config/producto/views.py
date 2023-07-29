from django.contrib import messages
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


# View para eliminar productos
def eliminar_producto(request, producto_id):
    if request.method == 'POST':
        producto = get_object_or_404(Producto, id=producto_id)
        producto.delete()
        messages.success(request, 'Producto eliminado exitosamente.')
        return redirect('listar_productos')
    else:
        return redirect('listar_productos')

#test

# View para confirmar eliminación de producto
def eliminar_producto_confirmacion(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    return render(request, 'confirmar_eliminacion.html', {'producto': producto})


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
