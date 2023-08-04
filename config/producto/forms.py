from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Producto


class ProductoForm(forms.ModelForm):
    class Meta:  # clase meta para establecer las caracteristicas del formulario ProductoForm
        model = Producto  # modelo al que pertenece el formulario
        fields = ['nombre', 'precio', 'descripcion', 'fecha_vencimiento', 'fabrica']  # campos que llevara el formulario
        labels = {
            'nombre': 'Nombre',  # el atributo del objeto es el key y el value es el label
            'precio': 'Precio',
            'descripcion': 'Descripción',
            'fecha_vencimiento': 'Fecha de Vencimiento',
            'fabrica': 'Fábrica'
        }
        widgets = {  # caracteristicas de los campos a mostrar en el formulario
            'nombre': forms.TextInput(attrs={'class': 'form-control w-100'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control w-100'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control w-100'}),
            'fecha_vencimiento': forms.DateInput(attrs={'class': 'form-control w-100', 'type': 'date'}),
            'fabrica': forms.Select(attrs={'class': 'form-control w-100'})
        }


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        label='Email',
        help_text='Enter a valid email address. Only letters, digits and @/./+/-/_ characters are allowed.',
        required=True)  # Add email field

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['username'].label = 'Nombre de usuario'
        # self.fields['password1'].label = 'Contraseña'
        # self.fields['password2'].label = 'Confirmar contraseña'
        # self.error_messages['password_mismatch'] = 'Las contraseñas no coinciden.'
