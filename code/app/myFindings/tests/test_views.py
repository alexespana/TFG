from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from myFindings.models import Excavacion, Hecho, Estancia

class TestListingViews(TestCase):

    def setUp(self):
        User.objects.create_superuser(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')

    def test_list_excavations_GET(self):
        response = self.client.get(reverse('excavations'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'excavations_list.html')

    def test_list_sedimentaryues_GET(self):
        response = self.client.get(reverse('sedimentaryues'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'sedimentaryues_list.html')

    def test_list_builtues_GET(self):
        response = self.client.get(reverse('builtues'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'builtues_list.html')

    def test_list_facts_GET(self):
        response = self.client.get(reverse('facts'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'facts_list.html')

    def test_list_rooms_GET(self):
        response = self.client.get(reverse('rooms'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'rooms_list.html')

    def test_list_photos_GET(self):
        response = self.client.get(reverse('photos'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'photos_list.html')

    def test_list_inclusions_GET(self):
        response = self.client.get(reverse('inclusions'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'inclusions_list.html')

    def test_list_sedimentarymaterials_GET(self):
        response = self.client.get(reverse('sedimentarymaterials'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'sedimentarymaterials_list.html')

    def test_list_builtmaterials_GET(self):
        response = self.client.get(reverse('builtmaterials'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'builtmaterials_list.html')

    def test_list_excavationues_GET(self):
        Excavacion.objects.create(
            n_excavacion=1,
            latitud=1,
            longitud=1,
            altura=1
        )
        response = self.client.get(reverse('excavationues', kwargs={'id': 1}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'excavationues.html')

    def test_list_roomfacts_GET(self):
        Estancia.objects.create(
            n_estancia=1,
        )
        response = self.client.get(reverse('roomfacts', kwargs={'id': 1}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'facts_list.html')

    def test_list_factues_GET(self):
        Hecho.objects.create(
            letra='MR',
            numero='000001'
        )
        response = self.client.get(reverse('factues', kwargs={'id': 1}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'excavationues.html')
