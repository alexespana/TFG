from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from myFindings.models import Excavacion, Fotografia, Hecho, Estancia, Inclusion, \
                              MaterialConstruida, MaterialSedimentaria, UESedimentaria, UEConstruida

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
        pk=Excavacion.objects.create(
            n_excavacion=1,
            latitud=1,
            longitud=1,
            altura=1,
        ).pk

        response = self.client.get(reverse('excavationues', kwargs={'id': pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'excavationues.html')

    def test_list_roomfacts_GET(self):
        pk=Estancia.objects.create(
            n_estancia=1,
        ).pk
        response = self.client.get(reverse('roomfacts', kwargs={'id': pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'facts_list.html')

    def test_list_factues_GET(self):
        pk = Hecho.objects.create(
            letra='MR',
            numero='000001'
        ).pk
        response = self.client.get(reverse('factues', kwargs={'id': pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'excavationues.html')

class TestAddViews(TestCase):
    def setUp(self):
        User.objects.create_superuser(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
        self.excavation = Excavacion.objects.create(
            n_excavacion=1,
            latitud=1,
            longitud=1,
            altura=1
        )

    def test_add_excavation_POST(self):
        response = self.client.post(reverse('add_excavation'), {
            'n_excavacion': 2,
            'latitud': 2,
            'longitud': 2,
            'altura': 2
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Excavacion.objects.count(), 2)

    def test_add_sedimentaryue_POST(self):
        response = self.client.post(reverse('add_sedimentaryue'), {
            'codigo': '000001',
            'excavacion': self.excavation,
            'descripcion': 'Sedimento',
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(UESedimentaria.objects.count(), 1)

    def test_add_builtue_POST(self):
        response = self.client.post(reverse('add_builtue'), {
            'codigo': '000001',
            'excavacion': self.excavation,
            'descripcion': 'Construcción',
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(UEConstruida.objects.count(), 1)

    def test_add_fact_POST(self):
        response = self.client.post(reverse('add_fact'), {
            'letra': 'MR',
            'numero': '000001',
            'comentarios': 'Hecho',
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Hecho.objects.count(), 1)

    def test_add_room_POST(self):
        response = self.client.post(reverse('add_room'), {
            'n_estancia': 1,
            'observaciones': 'This room is the largest',
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Estancia.objects.count(), 1)

    def test_add_photo_POST(self):
        response = self.client.post(reverse('add_photo'), {
            'numero': 1
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Fotografia.objects.count(), 1)

    def test_add_inclusion_POST(self):
        UESedimentaria.objects.create(
            codigo='000001',
            excavacion=self.excavation,
            descripcion='Descripcion 1'
        )
        response = self.client.post(reverse('add_inclusion'), {
            'tipo': 'Cenizas',
            'uesedimentaria': UESedimentaria.objects.get(codigo='000001').pk,
            'frecuencia': 'Ausencia',
            'grosor': '2-6 cm',
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Inclusion.objects.count(), 1)

    def test_add_sedimentarymaterial_POST(self):
        response = self.client.post(reverse('add_sedimentarymaterial'), {
            'nombre': 'New material',
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(MaterialSedimentaria.objects.count(), 10)

    def test_add_builtmaterial_POST(self):
        response = self.client.post(reverse('add_builtmaterial'), {
            'nombre': 'New material',
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(MaterialConstruida.objects.count(), 7)
