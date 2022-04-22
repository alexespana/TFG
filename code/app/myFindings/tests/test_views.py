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


class TestModifierViews(TestCase):

    def setUp(self):
        User.objects.create_superuser(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
        self.excavation = Excavacion.objects.create(
            n_excavacion=1,
            latitud=1,
            longitud=1,
            altura=1
        )

    def test_modify_excavation_POST(self):
        pkexcavation = Excavacion.objects.create(
            n_excavacion=2,
            latitud=2,
            longitud=2,
            altura=2
        ).pk
        response = self.client.post(reverse('modify_excavation', kwargs={'id': pkexcavation}), {
            'n_excavacion': 3,
            'latitud': 3,
            'longitud': 3,
            'altura': 3
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Excavacion.objects.get(pk=pkexcavation).n_excavacion, 3)

    def test_modify_fact_POST(self):
        pk = Hecho.objects.create(
            letra='MR',
            numero='000001',
            comentarios='Hecho',
        ).pk
        response = self.client.post(reverse('modify_fact', kwargs={'id': pk}), {
            'letra': 'MR',
            'numero': '000002',
            'comentarios': 'Hecho 2',
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Hecho.objects.get(pk=pk).numero, '000002')

    def test_modify_room_POST(self):
        pk = Estancia.objects.create(
            n_estancia='ES001',
            observaciones='This room is the largest',
        ).pk
        response = self.client.post(reverse('modify_room', kwargs={'id': pk}), {
            'n_estancia': 'ES002',
            'observaciones': 'This room is the smallest',
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Estancia.objects.get(pk=pk).n_estancia, 'ES002')

    def test_modify_photo_POST(self):
        pkroom = Estancia.objects.create(
            n_estancia='ES001',
            observaciones='This room is the largest',
        ).pk
        pk = Fotografia.objects.create(
            numero=1,
            estancia=Estancia.objects.get(pk=pkroom)
        ).pk
        response = self.client.post(reverse('modify_photo', kwargs={'id': pk}), {
            'numero': 2,
            'estancia': Estancia.objects.get(pk=pkroom).pk,
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Fotografia.objects.get(pk=pk).numero, 2)

    def test_modify_inclusion_POST(self):
        pkue = UESedimentaria.objects.create(
            codigo='000001',
            excavacion=self.excavation,
            descripcion='Sedimento',
        ).pk
    
        pk = Inclusion.objects.create(
            tipo='Cenizas',
            uesedimentaria=UESedimentaria.objects.get(pk=pkue),
            frecuencia='Ausencia',
            grosor='< 2 cm',
        ).pk
        response = self.client.post(reverse('modify_inclusion', kwargs={'id': pk}), {
            'tipo': 'Carbones',
            'uesedimentaria': UESedimentaria.objects.get(pk=pkue).pk,
            'frecuencia': 'Ocasional',
            'grosor': '2-6 cm',
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Inclusion.objects.get(pk=pk).grosor, '2-6 cm')

class TestEliminatingViews(TestCase):
    def setUp(self):
        User.objects.create_superuser(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
        self.excavation = Excavacion.objects.create(
            n_excavacion=1,
            latitud=1,
            longitud=1,
            altura=1
        )

    def test_delete_excavation_DELETE(self):
        response = self.client.delete(reverse('delete_excavation', kwargs={'id': self.excavation.pk}))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Excavacion.objects.count(), 0)

    def test_delete_fact_DELETE(self):
        pk = Hecho.objects.create(
            letra='MR',
            numero='000001',
            comentarios='Hecho',
        ).pk
        response = self.client.delete(reverse('delete_fact', kwargs={'id': pk}))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Hecho.objects.count(), 0)

    def test_delete_room_DELETE(self):
        pk = Estancia.objects.create(
            n_estancia='ES001',
            observaciones='This room is the largest',
        ).pk
        response = self.client.delete(reverse('delete_room', kwargs={'id': pk}))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Estancia.objects.count(), 0)

    def test_delete_photo_DELETE(self):
        pkroom = Estancia.objects.create(
            n_estancia='ES001',
        ).pk
        pk = Fotografia.objects.create(
            numero=1,
            estancia=Estancia.objects.get(pk=pkroom)
        ).pk
        response = self.client.delete(reverse('delete_photo', kwargs={'id': pk}))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Fotografia.objects.count(), 0)

    def test_delete_inclusion_DELETE(self):
        pkue = UESedimentaria.objects.create(
            codigo='000001',
            excavacion=Excavacion.objects.get(pk=self.excavation.pk),
            descripcion='Sedimento',
        ).pk  
        pk = Inclusion.objects.create(
            tipo='Cenizas',
            uesedimentaria=UESedimentaria.objects.get(pk=pkue),
            frecuencia='Ausencia',
            grosor='< 2 cm',
        ).pk
        response = self.client.delete(reverse('delete_inclusion', kwargs={'id': pk}))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Inclusion.objects.count(), 0)

    def test_delete_sedimentarymaterial_DELETE(self):
        pk = MaterialSedimentaria.objects.create(
            nombre='New material'
        ).pk
        response = self.client.delete(reverse('delete_sedimentarymaterial', kwargs={'nombre': pk}))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(MaterialSedimentaria.objects.count(), 9)

    def test_delete_builtmaterial_DELETE(self):
        pk = MaterialConstruida.objects.create(
            nombre='New material'
        ).pk
        response = self.client.delete(reverse('delete_builtmaterial', kwargs={'nombre': pk}))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(MaterialConstruida.objects.count(), 6)

    def test_delete_sedimentaryue_DELETE(self):
        pk = UESedimentaria.objects.create(
            codigo='000001',
            excavacion=Excavacion.objects.get(pk=self.excavation.pk),
            descripcion='Sedimento',
        ).pk
        response = self.client.delete(reverse('delete_sedimentaryue', kwargs={'id': pk}))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(UESedimentaria.objects.count(), 0)
    
    def test_delete_builtue_DELETE(self):
        pk = UEConstruida.objects.create(
            codigo='000001',
            excavacion=Excavacion.objects.get(pk=self.excavation.pk),
            descripcion='Construida',
        ).pk
        response = self.client.delete(reverse('delete_builtue', kwargs={'id': pk}))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(UEConstruida.objects.count(), 0)