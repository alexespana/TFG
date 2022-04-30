from rest_framework import status
from rest_framework.test import APITestCase
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from myFindings.models import Excavation, Photo, Fact, Room, Inclusion, \
                              BuiltMaterial, SedimentaryMaterial, SedimentaryUE, BuiltUE

class TestListingAPIViews(APITestCase):

    def test_api_list_excavations_GET(self):
        response = self.client.get(reverse('excavation-list', kwargs={}))
        self.assertEqual(response.status_code, 200)

    def test_api_list_photos_GET(self):
        response = self.client.get(reverse('photo-list', kwargs={}))
        self.assertEqual(response.status_code, 200)

    def test_api_list_facts_GET(self):
        response = self.client.get(reverse('fact-list', kwargs={}))
        self.assertEqual(response.status_code, 200)

    def test_api_list_rooms_GET(self):
        response = self.client.get(reverse('room-list', kwargs={}))
        self.assertEqual(response.status_code, 200)

    def test_api_list_inclusions_GET(self):
        response = self.client.get(reverse('inclusion-list', kwargs={}))
        self.assertEqual(response.status_code, 200)

    def test_api_list_sedimentarymaterials_GET(self):
        response = self.client.get(reverse('sedimentarymaterial-list', kwargs={}))
        self.assertEqual(response.status_code, 200)

    def test_api_list_builtmaterials_GET(self):
        response = self.client.get(reverse('builtmaterial-list', kwargs={}))
        self.assertEqual(response.status_code, 200)

    def test_api_list_sedimentaryues_GET(self):
        response = self.client.get(reverse('sedimentaryue-list', kwargs={}))
        self.assertEqual(response.status_code, 200)

    def test_api_list_builtues_GET(self):
        response = self.client.get(reverse('builtue-list', kwargs={}))
        self.assertEqual(response.status_code, 200)


class TestAddAPIViews(APITestCase):
    def setUp(self):
        self.excavation = Excavation.objects.create(
            n_excavacion='1',
            latitud=1,
            longitud=1,
            altura=1
        )

    def test_api_add_excavation_POST(self):
        response = self.client.post(reverse('excavation-list', kwargs={}),{
            'n_excavacion': '2',
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_api_add_photo_POST(self):
        response = self.client.post(reverse('photo-list', kwargs={}),{
            'numero': 2,
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_api_add_fact_POST(self):
        response = self.client.post(reverse('fact-list', kwargs={}),{
            'letra': 'MR',
            'numero': '001001'
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
    def test_api_add_room_POST(self):
        response = self.client.post(reverse('room-list', kwargs={}),{
            'n_estancia': '1',
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_api_add_inclusion_POST(self):
        SedimentaryUE.objects.create(
            n_orden='1',
            excavacion=self.excavation,
            descripcion='Descripcion 1'
        )
        response = self.client.post(reverse('inclusion-list', kwargs={}),{
            'tipo': 'Cenizas',
            'uesedimentaria': SedimentaryUE.objects.get(codigo='001001').pk,
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_api_add_sedimentarymaterial_POST(self):
        response = self.client.post(reverse('sedimentarymaterial-list', kwargs={}),{
            'nombre': 'Material 1',
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_api_add_builtmaterial_POST(self):
        response = self.client.post(reverse('builtmaterial-list', kwargs={}),{
            'nombre': 'Material 1',
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_api_add_sedimentaryue_POST(self):
        response = self.client.post(reverse('sedimentaryue-list', kwargs={}),{
            'n_orden': '1',
            'excavacion': self.excavation.n_excavacion,
            'descripcion': 'Sedimento',
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_api_add_builtue_POST(self):
        response = self.client.post(reverse('builtue-list', kwargs={}),{
            'n_orden': '1',
            'excavacion': self.excavation.n_excavacion,
            'descripcion': 'Material',
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class TestUpdateAPIViews(APITestCase): 
    def setUp(self):
        self.excavation = Excavation.objects.create(
            n_excavacion='1',
            latitud=1,
            longitud=1,
            altura=1
        )
        self.room = Room.objects.create(
            n_estancia='1',
            observaciones='This room is the largest',
        )
        self.sedimentaryue = SedimentaryUE.objects.create(
            n_orden='1',
            excavacion=self.excavation,
            descripcion='Sedimentaria',
        )   

    def test_api_update_excavation_PUT(self):
        response = self.client.put(reverse('excavation-detail', kwargs={'pk': self.excavation.pk}),{
            'n_excavacion': '1',
            'altura': 2,
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Excavation.objects.get(pk=self.excavation.pk).altura, 2)

    def test_api_update_photo_PUT(self):
        pk = Photo.objects.create(
            numero=1,
            estancia=self.room
        ).pk
        response = self.client.put(reverse('photo-detail', kwargs={'pk': pk}),{
            'numero': 2,
            'estancia': Room.objects.get(pk=self.room.pk).pk,
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Photo.objects.get(pk=pk).numero, 2)

    def test_api_update_fact_PUT(self):
        pk = Fact.objects.create(
            letra='MR',
            numero='001001',
            estancia=self.room,
            comentarios='This is a comment'
        ).pk
        response = self.client.put(reverse('fact-detail', kwargs={'pk': pk}),{
            'letra': 'MR',
            'numero': '001001',
            'n_estancia': self.room,
            'comentarios': 'This is the comment 2'
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Fact.objects.get(pk=pk).comentarios, 'This is the comment 2')

    def test_api_update_room_PUT(self):
        response = self.client.put(reverse('room-detail', kwargs={'pk': self.room.pk}),{
            'n_estancia': '1',
            'observaciones': 'This room is the smallest',
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Room.objects.get(pk=self.room.pk).observaciones, 'This room is the smallest')
    
    def test_api_update_inclusion_PUT(self):
        pk = Inclusion.objects.create(
            tipo='Cenizas',
            uesedimentaria=self.sedimentaryue,
            frecuencia='Medio',
        ).pk
        response = self.client.put(reverse('inclusion-detail', kwargs={'pk': pk}),{
            'tipo': 'Cenizas',
            'uesedimentaria': SedimentaryUE.objects.get(pk=self.sedimentaryue.pk).pk,
            'frecuencia': 'Ocasional',
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Inclusion.objects.get(pk=pk).frecuencia, 'Ocasional')

    def test_api_update_sedimentaryue_PUT(self):
        response = self.client.put(reverse('sedimentaryue-detail', kwargs={'codigo': self.sedimentaryue.codigo}),{
            'n_orden': '1',
            'excavacion': self.excavation.n_excavacion,
            'descripcion': 'Sedimento',
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(SedimentaryUE.objects.get(pk=self.sedimentaryue.pk).descripcion, 'Sedimento')

    def test_api_update_builtue_PUT(self):
        pk = BuiltUE.objects.create(
            n_orden='2',
            excavacion=Excavation.objects.get(pk=self.excavation.pk),
            descripcion='Construida',
        ).pk
        response = self.client.put(reverse('builtue-detail', kwargs={'codigo': BuiltUE.objects.get(pk=pk).codigo}),{
            'n_orden': '2',
            'excavacion': self.excavation.n_excavacion,
            'descripcion': 'Construida con metal',
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(BuiltUE.objects.get(pk=pk).descripcion, 'Construida con metal')
    
class TestDeleteAPIViews(APITestCase):
    def setUp(self):
        self.excavation = Excavation.objects.create(
            n_excavacion='1',
            latitud=1,
            longitud=1,
            altura=1
        )
        self.room = Room.objects.create(
            n_estancia='1',
            observaciones='This room is the largest',
        )
        self.sedimentaryue = SedimentaryUE.objects.create(
            n_orden='1',
            excavacion=self.excavation,
            descripcion='Sedimentaria',
        )   

    def test_api_delete_excavation_DELETE(self):
        response = self.client.delete(reverse('excavation-detail', kwargs={'pk': self.excavation.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Excavation.objects.filter(pk=self.excavation.pk).count(), 0)

    def test_api_delete_photo_DELETE(self):
        pk = Photo.objects.create(
            numero=1,
            estancia=self.room
        ).pk
        response = self.client.delete(reverse('photo-detail', kwargs={'pk': pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Photo.objects.filter(pk=pk).count(), 0)

    def test_api_delete_fact_DELETE(self):
        pk = Fact.objects.create(
            letra='MR',
            numero='001001',
            estancia=self.room,
            comentarios='This is a comment'
        ).pk
        response = self.client.delete(reverse('fact-detail', kwargs={'pk': pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Fact.objects.filter(pk=pk).count(), 0)

    def test_api_delete_room_DELETE(self):
        response = self.client.delete(reverse('room-detail', kwargs={'pk': self.room.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Room.objects.filter(pk=self.room.pk).count(), 0)

    def test_api_delete_inclusion_DELETE(self):
        pk = Inclusion.objects.create(
            tipo='Cenizas',
            uesedimentaria=self.sedimentaryue,
            frecuencia='Medio',
        ).pk
        response = self.client.delete(reverse('inclusion-detail', kwargs={'pk': pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Inclusion.objects.filter(pk=pk).count(), 0)

    def test_api_delete_sedimentaryue_DELETE(self):
        response = self.client.delete(reverse('sedimentaryue-detail', kwargs={'codigo': self.sedimentaryue.codigo}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(SedimentaryUE.objects.filter(pk=self.sedimentaryue.pk).count(), 0)

    def test_api_delete_builtue_DELETE(self):
        pk = BuiltUE.objects.create(
            n_orden='2',
            excavacion=self.excavation,
            descripcion='Construida',
        ).pk
        response = self.client.delete(reverse('builtue-detail', kwargs={'codigo': BuiltUE.objects.get(pk=pk).codigo}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(BuiltUE.objects.filter(pk=pk).count(), 0)
