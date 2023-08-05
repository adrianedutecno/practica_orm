import logging

from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.test import TestCase
from django.test import SimpleTestCase

from django.urls import reverse

from .models import Fabrica, Producto


# Create your tests here.
class ViewTest(TestCase):
    databases = ['default']  # Include the database

    @classmethod
    def setUp(self):
        self.logger = logging.getLogger(__name__)
        self.fabrica = Fabrica.objects.create(nombre="Fabrica 1")
        self.producto = Producto.objects.create(nombre="Producto 1", precio=100, descripcion="Desc 1",
                                                fabrica_id=self.fabrica.id)

    def test_listar_productos(self):
        response = self.client.get(reverse('listar_productos'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'listar_productos.html')
        self.assertContains(response, 'Producto 1')

    def test_crear_producto(self):
        fabrica = Fabrica.objects.create(nombre="Fabrica")
        print("Fabrica ID test_crear_producto:", fabrica.id)
        response = self.client.post(reverse('crear_producto'), {
            'nombre': 'Nuevo Producto',
            'precio': 100,
            'descripcion': 'Descripción del nuevo producto',
            'fecha_vencimiento': '',
            'fabrica': fabrica.id,
        })
        # print("Fabrica nombre test_crear_producto:", Producto.objects.get(id=4).nombre)
        self.assertEqual(response.status_code, 302)  # Redirect after successful form submission
        self.assertEqual(Producto.objects.count(), 2)
        self.assertIsNotNone(response)
        # self.assertEqual(Producto.objects.get(id=4).nombre, 'Nuevo Producto')

    #
    def test_editar_producto(self):
        fabrica = Fabrica.objects.create(nombre="Fabrica")
        producto = Producto.objects.create(nombre='Producto a editar', precio=150, descripcion='Descripción original',
                                           fabrica_id=fabrica.id)

        response = self.client.post(reverse('editar_producto', args=[producto.id]), {
            'nombre': 'Producto editado',
            'precio': 200,
            'fecha_vencimiento': '',
            'descripcion': 'Nueva descripción',
            'fabrica': fabrica.id,
        })

        self.assertEqual(response.status_code, 302)
        producto.refresh_from_db()
        self.assertEqual(producto.nombre, 'Producto editado')

    def test_buscar(self):
        fabrica1 = Fabrica.objects.create(nombre="Fabrica 1")
        # fabrica2 = Fabrica.objects.create(nombre="Fabrica 2")
        Producto.objects.create(nombre="Producto 1", precio=100, descripcion="Desc 1", fabrica=fabrica1)
        # Producto.objects.create(nombre="Producto 2", precio=200, descripcion="Desc 2", fabrica=fabrica2)

        response = self.client.get(reverse('buscar'), {'query': 'Producto'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'buscar.html')
        self.assertContains(response, 'Producto 1')
        # self.assertContains(response, 'Producto 2')

    def test_eliminar(self):
        fabrica = Fabrica.objects.create(nombre="Fabrica")
        producto = Producto.objects.create(nombre="Producto", precio=100, descripcion="Desc", fabrica=fabrica)

        response = self.client.post(reverse('eliminar', args=[producto.id]))

        self.assertEqual(response.status_code, 302)  # Redirect after successful deletion
        self.assertFalse(Producto.objects.filter(id=producto.id).exists())

    #
    def test_eliminar_confirmacion(self):
        fabrica = Fabrica.objects.create(nombre="Fabrica")
        producto = Producto.objects.create(nombre="Producto a confirmar", precio=100, descripcion="Desc",
                                           fabrica=fabrica)

        response = self.client.get(reverse('eliminar_confirmacion', args=[producto.id]))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'confirmar.html')
        self.assertContains(response, 'Producto a confirmar')

    #
    # def test_registro(self):
    #     response = self.client.post(reverse('registro'), {
    #         'username': 'newuser',
    #         'email': 'e@e.cl',
    #         'password1': 'newpassword',
    #         'password2': 'newpassword',
    #     })
    #
    #     self.assertEqual(response.status_code, 302)  # Redirect after successful form submission
    #     self.assertTrue(User.objects.filter(username='newuser').exists())
    #
    # def test_iniciar_sesion_valid_user(self):
    #     user = get_user_model().objects.create_user(username='testuser', password='testpass')
    #
    #     response = self.client.post(reverse('iniciar_sesion'), {
    #         'username': 'testuser',
    #         'password': 'testpass',
    #     })
    #
    #     self.assertEqual(response.status_code, 302)  # Redirect after successful login
    #     self.assertIn('_auth_user_id', self.client.session)
    #
    # def test_iniciar_sesion_invalid_user(self):
    #     response = self.client.post(reverse('iniciar_sesion'), {
    #         'username': 'invaliduser',
    #         'password': 'invalidpass',
    #     })
    #
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'login.html')
    #     self.assertContains(response, 'Usuario o password inválidas')
    #
    # def test_cerrar_sesion(self):
    #     user = get_user_model().objects.create_user(username='testuser', password='testpass')
    #     self.client.login(username='superuser', password='admin')
    #
    #     response = self.client.get(reverse('cerrar_sesion'))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'login.html')
    #     self.assertNotIn('_auth_user_id', self.client.session)
    #


class TemplateTest(TestCase):

    def test_listar_productos(self):
        response = self.client.get(reverse('listar_productos'))
        self.assertEqual(response.status_code, 200)

    def test_crear_producto(self):
        response = self.client.get(reverse('crear_producto'))
        self.assertEqual(response.status_code, 200)

    def test_editar_producto(self):
        self.fabrica = Fabrica.objects.create(nombre="Fabrica 1")
        self.producto = Producto.objects.create(nombre="Producto 1", precio=100, descripcion="Desc 1",
                                                fabrica_id=self.fabrica.id)
        print("Fabrica test_editar_producto:", self.fabrica)
        response = self.client.get(reverse('editar_producto', args=[self.fabrica.id]))
        print("RESPONSE test_editar_producto:", response)
        self.assertEqual(response.status_code, 200)

    def test_eliminar_confirmacion(self):
        self.fabrica = Fabrica.objects.create(nombre="Fabrica 1")
        self.producto = Producto.objects.create(nombre="Producto 1", precio=100, descripcion="Desc 1",
                                                fabrica_id=self.fabrica.id)
        print("Fabrica test_eliminar_confirmacion:", self.fabrica)
        response = self.client.get(reverse('eliminar_confirmacion', args=[self.producto.id]))
        print("RESPONSE test_eliminar_confirmacion:", response)
        self.assertEqual(response.status_code, 200)

    def test_eliminar(self):
        self.fabrica = Fabrica.objects.create(nombre="Fabrica 1")
        self.producto = Producto.objects.create(nombre="Producto 1", precio=100, descripcion="Desc 1",
                                                fabrica_id=self.fabrica.id)
        print("Fabrica test_eliminar:", self.fabrica)
        response = self.client.post(reverse('eliminar', args=[self.producto.id]))
        print("RESPONSE test_eliminar:", response)
        self.assertEqual(response.status_code, 302)  # Expecting a redirect after successful deletion

    def test_cerrar_sesion(self):
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 200)  # You might customize this based on your logout logic

    def test_iniciar_sesion(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    def test_registro(self):
        response = self.client.get(reverse('registro'))
        self.assertEqual(response.status_code, 200)

    def test_buscar(self):
        response = self.client.get(reverse('buscar'), {'query': 'Producto'})
        self.assertEqual(response.status_code, 200)


class ReboundTest(TestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get(reverse('crear_producto'))
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse('crear_producto'))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        response = self.client.get(reverse('crear_producto'))
        self.assertTemplateUsed(response, "crear_producto.html")

    def test_template_content(self):
        response = self.client.get(reverse('crear_producto'))
        self.assertContains(response, '<h2>Crear producto</h2>')
        self.assertNotContains(response, 'No es la Página')


class DrillingTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.fabrica = Fabrica.objects.create(nombre='Fabrica1', pais='Argentina')
        cls.producto = Producto.objects.create(nombre="producto1", precio='123546', descripcion='Descripcion P1',
                                               fecha_vencimiento='2023-12-01', fabrica_id="1")

    def test_model_content_fabrica(self):
        self.assertEqual(self.fabrica.nombre, "Fabrica1")
        self.assertEqual(self.fabrica.pais, "Argentina")

    def test_model_content_producto(self):
        self.assertEqual(self.producto.nombre, "producto1")
        self.assertEqual(self.producto.precio, "123546")
        self.assertEqual(self.producto.descripcion, "Descripcion P1")
        self.assertEqual(self.producto.fecha_vencimiento, "2023-12-01")
        self.assertEqual(self.producto.fabrica_id, "1")

    def test_url_exists_at_correct_location(self):
        response = self.client.get(reverse('listar_productos'))
        self.assertEqual(response.status_code, 200)

    def test_mostrarpage(self):
        response = self.client.get(reverse('listar_productos'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'listar_productos.html')
        self.assertContains(response, '<h2 class="d-inline-flex">Lista Productos</h2>')
