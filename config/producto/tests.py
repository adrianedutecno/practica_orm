from django.test import TestCase
from django.urls import reverse

from .models import Fabrica, Producto


class TemplateTest(TestCase):

    def setUp(self):
        # Setup run before every test method
        # fabrica
        self.fabrica = Fabrica.objects.create(nombre='Fabrica')
        # producto
        self.producto = Producto.objects.create(nombre='Producto',
                                                precio=1500,
                                                descripcion='Descripcion',
                                                fecha_vencimiento='2023-08-05',
                                                fabrica_id=self.fabrica.id)

    def test_listar_productos(self):
        response = self.client.get(reverse('listar_productos'))
        print('RESPONSE:', response)
        self.assertEqual(response.status_code, 200)  # test response status code 200 OK
        self.assertTemplateUsed(response, 'listar_productos.html')  # test render template listar_productos.html

    def test_crear_producto(self):
        response = self.client.get(reverse('crear_producto'))
        self.assertIsNotNone(response)
        self.assertEqual(response.status_code, 200)  # test response status code 200 OK
        self.assertTemplateUsed(response, 'crear_producto.html')  # test render template crear_producto.html

    def test_editar_producto(self):
        # # fabrica
        # self.fabrica = Fabrica.objects.create(nombre='Fabrica')
        # # producto
        # self.producto = Producto.objects.create(nombre='Producto',
        #                                         precio=1500,
        #                                         descripcion='Descripcion',
        #                                         fecha_vencimiento='2023-08-05',
        #                                         fabrica_id=self.fabrica.id)

        response = self.client.get(reverse('editar_producto', args=[self.producto.id]))
        self.assertEqual(response.status_code, 200)  # test response status code 200 OK
        self.assertTemplateUsed(response, 'editar_producto.html')  # test render template editar_producto.html

    def test_eliminar_confirmacion(self):
        # # fabrica
        # self.fabrica = Fabrica.objects.create(nombre='Fabrica')
        # # producto
        # self.producto = Producto.objects.create(nombre='Producto',
        #                                         precio=1500,
        #                                         descripcion='Descripcion',
        #                                         fecha_vencimiento='2023-08-05',
        #                                         fabrica_id=self.fabrica.id)

        response = self.client.get(reverse('eliminar_confirmacion', args=[self.producto.id]))
        self.assertEqual(response.status_code, 200)  # test response status code 200 OK
        self.assertTemplateUsed(response, 'confirmar.html')  # test render template editar_producto.html

    def test_elminar(self):
        # # fabrica
        # self.fabrica = Fabrica.objects.create(nombre='Fabrica')
        # # producto
        # self.producto = Producto.objects.create(nombre='Producto',
        #                                         precio=1500,
        #                                         descripcion='Descripcion',
        #                                         fecha_vencimiento='2023-08-05',
        #                                         fabrica_id=self.fabrica.id)

        response = self.client.get(reverse('eliminar', args=[self.producto.id]))
        self.assertEqual(response.status_code, 302)  # test redirect response status code 302 FOUND

    def test_cerrar_sesion(self):
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_iniciar_sesion(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_registro(self):
        response = self.client.get(reverse('registro'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registro.html')

    def test_buscar(self):
        response = self.client.get(reverse('buscar'), {'query': 'Producto'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'buscar.html')
        self.assertContains(response, '<h2>Resultado Busqueda</h2>')
        # self.assertContains(response, '<p>No hay Productos disponibles para la busqueda</p>')
        self.assertNotContains(response, '<p>No hay Productos disponibles para la busqueda</p>')
        self.assertContains(response, '<section class="container mt-5">')
        self.assertContains(response, '<th scope="col">Id</th>')
        self.assertContains(response, 'Producto')
