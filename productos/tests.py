from rest_framework import status
from rest_framework.test import APITestCase

from django.contrib.auth.models import User

from .models import Articulo, Proveedor



# Al iniciarse los tests, se crea una DB volatil exclusiva para el test.
class ArticuloTests(APITestCase):
    def setUp(self):
        self.usuario = User.objects.create_user(username='pepe', password='1234')
        self.proveedor = Proveedor.objects.create(nombre='Razer', telefono='1234567')
        self.articulo = Articulo.objects.create(nombre='Teclado mecánico', precio=1500, stock=50, proveedor=self.proveedor)
        self.url = '/api/articulos/'

    def test_listar_articulos_sin_auth(self):
        response = self.client.get(self.url)

        # breakpoint()
        #ASSERT despues de la peticion -> Si obtuve un 200 -> True TEST PASSED
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_crear_articulo_sin_auth(self):
        data = dict(nombre='Teclado mecánico', precio=1500, stock=50, proveedor=self.proveedor)
        response = self.client.post(self.url, data)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_crear_articulo_con_auth(self):
        self.client.login(username='pepe', password='1234')

        data = {'nombre': 'Teclado mecánico', 'precio': 1500, 'stock': 50, 'proveedor': 1}
        response = self.client.post(self.url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
