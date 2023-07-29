from django import forms

from .models import Producto


class ProductoForm(forms.ModelForm):
    class Meta:  # clase meta para establecer las caracteristicas del formulario ProductoForm
        model = Producto  # modelo al que pertenece el formulario
        fields = ['nombre', 'precio', 'descripcion', 'fecha_vencimiento', 'fabrica']  # campos que llevara el formulario
        labels = {
            'nombre': 'Nombre',  # el atributo del objeto es el key y el value es el label
            'precio': 'Precio',
            'descripcion': 'Descripción',
            'fecha_vencimiento' : 'Fecha de Vencimiento',
            'fabrica': 'Fábrica'
        }
        widgets = {  # caracteristicas de los campos a mostrar en el formulario
            'nombre': forms.TextInput(attrs={'class': 'form-control w-100'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control w-100'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control w-100'}),
            'fecha_vencimiento': forms.DateInput(attrs={'class': 'form-control w-100', 'type': 'date'}),
            'fabrica': forms.Select(attrs={'class': 'form-control w-100'})
        }
