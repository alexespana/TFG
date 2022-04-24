from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from myFindings.models import Excavation, Photo, Fact, Room, Inclusion, \
                              BuiltMaterial, SedimentaryMaterial, SedimentaryUE, BuiltUE

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
        pk=Excavation.objects.create(
            n_excavacion='1',
            latitud=1,
            longitud=1,
            altura=1,
        ).pk

        response = self.client.get(reverse('excavationues', kwargs={'id': pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'excavationues.html')

    def test_list_roomfacts_GET(self):
        pk=Room.objects.create(
            n_estancia='1',
        ).pk
        response = self.client.get(reverse('roomfacts', kwargs={'id': pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'facts_list.html')

    def test_list_factues_GET(self):
        pk = Fact.objects.create(
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
        self.excavation = Excavation.objects.create(
            n_excavacion='1',
            latitud=1,
            longitud=1,
            altura=1
        )

    def test_add_excavation_POST(self):
        response = self.client.post(reverse('add_excavation'), {
            'n_excavacion': '2',
            'latitud': 2,
            'longitud': 2,
            'altura': 2
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Excavation.objects.count(), 2)

    def test_add_sedimentaryue_POST(self):
        response = self.client.post(reverse('add_sedimentaryue'), {
            'n_orden': '1',
            'excavacion': self.excavation,
            'descripcion': 'Sedimento',
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(SedimentaryUE.objects.count(), 1)

    def test_add_builtue_POST(self):
        response = self.client.post(reverse('add_builtue'), {
            'n_orden': '1',
            'excavacion': self.excavation,
            'descripcion': 'Construcción',
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(BuiltUE.objects.count(), 1)

    def test_add_fact_POST(self):
        response = self.client.post(reverse('add_fact'), {
            'letra': 'MR',
            'numero': '000001',
            'comentarios': 'Fact',
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Fact.objects.count(), 1)

    def test_add_room_POST(self):
        response = self.client.post(reverse('add_room'), {
            'n_estancia': '1',
            'observaciones': 'This room is the largest',
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Room.objects.count(), 1)

    def test_add_photo_POST(self):
        response = self.client.post(reverse('add_photo'), {
            'numero': 1
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Photo.objects.count(), 1)

    def test_add_inclusion_POST(self):
        SedimentaryUE.objects.create(
            n_orden='1',
            excavacion=self.excavation,
            descripcion='Descripcion 1'
        )
        response = self.client.post(reverse('add_inclusion'), {
            'tipo': 'Cenizas',
            'uesedimentaria': SedimentaryUE.objects.get(codigo='001001').pk,
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
        self.assertEqual(SedimentaryMaterial.objects.count(), 10)

    def test_add_builtmaterial_POST(self):
        response = self.client.post(reverse('add_builtmaterial'), {
            'nombre': 'New material',
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(BuiltMaterial.objects.count(), 7)


class TestModifierViews(TestCase):

    def setUp(self):
        User.objects.create_superuser(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
        self.excavation = Excavation.objects.create(
            n_excavacion=1,
            latitud=1,
            longitud=1,
            altura=1
        )

    def test_modify_excavation_POST(self):
        pkexcavation = Excavation.objects.create(
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
        self.assertEqual(Excavation.objects.get(pk=pkexcavation).n_excavacion, 3)

    def test_modify_fact_POST(self):
        pk = Fact.objects.create(
            letra='MR',
            numero='000001',
            comentarios='Fact',
        ).pk
        response = self.client.post(reverse('modify_fact', kwargs={'id': pk}), {
            'letra': 'MR',
            'numero': '000002',
            'comentarios': 'Fact 2',
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Fact.objects.get(pk=pk).numero, '000002')

    def test_modify_room_POST(self):
        pk = Room.objects.create(
            n_estancia='ES001',
            observaciones='This room is the largest',
        ).pk
        response = self.client.post(reverse('modify_room', kwargs={'id': pk}), {
            'n_estancia': 'ES002',
            'observaciones': 'This room is the smallest',
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Room.objects.get(pk=pk).n_estancia, 'ES002')

    def test_modify_photo_POST(self):
        pkroom = Room.objects.create(
            n_estancia='ES001',
            observaciones='This room is the largest',
        ).pk
        pk = Photo.objects.create(
            numero=1,
            estancia=Room.objects.get(pk=pkroom)
        ).pk
        response = self.client.post(reverse('modify_photo', kwargs={'id': pk}), {
            'numero': 2,
            'estancia': Room.objects.get(pk=pkroom).pk,
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Photo.objects.get(pk=pk).numero, 2)

    def test_modify_inclusion_POST(self):
        pkue = SedimentaryUE.objects.create(
            codigo='000001',
            excavacion=self.excavation,
            descripcion='Sedimento',
        ).pk
    
        pk = Inclusion.objects.create(
            tipo='Cenizas',
            uesedimentaria=SedimentaryUE.objects.get(pk=pkue),
            frecuencia='Ausencia',
            grosor='< 2 cm',
        ).pk
        response = self.client.post(reverse('modify_inclusion', kwargs={'id': pk}), {
            'tipo': 'Carbones',
            'uesedimentaria': SedimentaryUE.objects.get(pk=pkue).pk,
            'frecuencia': 'Ocasional',
            'grosor': '2-6 cm',
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Inclusion.objects.get(pk=pk).grosor, '2-6 cm')

    def test_modify_builtue_POST(self):
        pkexcavation = Excavation.objects.create(
            n_excavacion=21,
            latitud=21,
            longitud=21,
            altura=21
        ).pk
        pk = BuiltUE.objects.create(
            codigo='000021',
            excavacion=Excavation.objects.get(pk=pkexcavation),
            descripcion='Sedimento',
        ).pk
        response = self.client.post(reverse('modify_builtue', kwargs={'id': pk}), {
            'codigo': '000002',
            'excavacion': Excavation.objects.get(pk=pkexcavation),
            'descripcion': 'Construida',
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(BuiltUE.objects.get(pk=pk).codigo, '000002')

    def test_modify_sedimentaryue_POST(self):
        pkexcavation = Excavation.objects.create(
            n_excavacion=22,
            latitud=22,
            longitud=22,
            altura=22
        ).pk
        pk = SedimentaryUE.objects.create(
            codigo='000022',
            excavacion=Excavation.objects.get(pk=pkexcavation),
            descripcion='Sedimentaria',
        ).pk
        response = self.client.post(reverse('modify_sedimentaryue', kwargs={'id': pk}), {
            'codigo': '000023',
            'excavacion': Excavation.objects.get(pk=pkexcavation),
            'descripcion': 'Sedimento 2',
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(SedimentaryUE.objects.get(pk=pk).codigo, '000023')

class TestEliminatingViews(TestCase):
    def setUp(self):
        User.objects.create_superuser(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
        self.excavation = Excavation.objects.create(
            n_excavacion=1,
            latitud=1,
            longitud=1,
            altura=1
        )

    def test_delete_excavation_DELETE(self):
        response = self.client.delete(reverse('delete_excavation', kwargs={'id': self.excavation.pk}))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Excavation.objects.count(), 0)

    def test_delete_fact_DELETE(self):
        pk = Fact.objects.create(
            letra='MR',
            numero='000001',
            comentarios='Fact',
        ).pk
        response = self.client.delete(reverse('delete_fact', kwargs={'id': pk}))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Fact.objects.count(), 0)

    def test_delete_room_DELETE(self):
        pk = Room.objects.create(
            n_estancia='ES001',
            observaciones='This room is the largest',
        ).pk
        response = self.client.delete(reverse('delete_room', kwargs={'id': pk}))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Room.objects.count(), 0)

    def test_delete_photo_DELETE(self):
        pkroom = Room.objects.create(
            n_estancia='ES001',
        ).pk
        pk = Photo.objects.create(
            numero=1,
            estancia=Room.objects.get(pk=pkroom)
        ).pk
        response = self.client.delete(reverse('delete_photo', kwargs={'id': pk}))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Photo.objects.count(), 0)

    def test_delete_inclusion_DELETE(self):
        pkue = SedimentaryUE.objects.create(
            codigo='000001',
            excavacion=Excavation.objects.get(pk=self.excavation.pk),
            descripcion='Sedimento',
        ).pk  
        pk = Inclusion.objects.create(
            tipo='Cenizas',
            uesedimentaria=SedimentaryUE.objects.get(pk=pkue),
            frecuencia='Ausencia',
            grosor='< 2 cm',
        ).pk
        response = self.client.delete(reverse('delete_inclusion', kwargs={'id': pk}))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Inclusion.objects.count(), 0)

    def test_delete_sedimentarymaterial_DELETE(self):
        pk = SedimentaryMaterial.objects.create(
            nombre='New material'
        ).pk
        response = self.client.delete(reverse('delete_sedimentarymaterial', kwargs={'nombre': pk}))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(SedimentaryMaterial.objects.count(), 9)

    def test_delete_builtmaterial_DELETE(self):
        pk = BuiltMaterial.objects.create(
            nombre='New material'
        ).pk
        response = self.client.delete(reverse('delete_builtmaterial', kwargs={'nombre': pk}))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(BuiltMaterial.objects.count(), 6)

    def test_delete_sedimentaryue_DELETE(self):
        pk = SedimentaryUE.objects.create(
            codigo='000001',
            excavacion=Excavation.objects.get(pk=self.excavation.pk),
            descripcion='Sedimento',
        ).pk
        response = self.client.delete(reverse('delete_sedimentaryue', kwargs={'id': pk}))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(SedimentaryUE.objects.count(), 0)
    
    def test_delete_builtue_DELETE(self):
        pk = BuiltUE.objects.create(
            codigo='000001',
            excavacion=Excavation.objects.get(pk=self.excavation.pk),
            descripcion='Construida',
        ).pk
        response = self.client.delete(reverse('delete_builtue', kwargs={'id': pk}))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(BuiltUE.objects.count(), 0)