from django.test import TestCase, Client
from django.http import HttpResponse
from .views import saludo
from .views import despedida, dameFecha, calculaEdad

class SaludoViewTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_saludo_view(self):
        response = self.client.get('/saludo/')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response, HttpResponse)
        self.assertEqual(response.content, b'')  # Assuming 'documento' is empty
        class ViewTests(TestCase):
            def setUp(self):
                self.client = Client()

            def test_despedida_view(self):
                response = self.client.get('/despedida/')
                self.assertEqual(response.status_code, 200)
                self.assertIsInstance(response, HttpResponse)
                self.assertEqual(response.content, b'Hasta luego, mundo')

            def test_dameFecha_view(self):
                response = self.client.get('/dameFecha/')
                self.assertEqual(response.status_code, 200)
                self.assertIsInstance(response, HttpResponse)
                self.assertIn(b'Fecha y hora actuales', response.content)

            def test_calculaEdad_view(self):
                response = self.client.get('/calculaEdad/2030/')
                self.assertEqual(response.status_code, 200)
                self.assertIsInstance(response, HttpResponse)
                self.assertIn('En el año 2030 tendrás 38 años'.encode(), response.content)
