from django.test import TestCase
from django.contrib.auth.models import User
from myFindings.models import Excavation, Room, SedimentaryUE, BuiltUE, SedimentaryMaterial,\
                              BuiltMaterial, Inclusion, Fact, Photo

class TestAdminUrls(TestCase):
    def setUp(self):
        User.objects.create_superuser(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')

    def test_initial_page(self):
        response = self.client.get('/admin/')
        self.assertEqual(response.status_code, 200)

    def test_initial_page_login(self):
        response = self.client.get('/admin/login/')
        self.assertEqual(response.status_code, 302)

    def test_initial_page_logout(self):
        response = self.client.get('/admin/logout/')
        self.assertEqual(response.status_code, 200)

    def test_users_page(self):
        response = self.client.get('/admin/auth/user/')
        self.assertEqual(response.status_code, 200)

    def test_groups_page(self):
        response = self.client.get('/admin/auth/group/')
        self.assertEqual(response.status_code, 200)


class TestModelsAdmin(TestCase):
    def setUp(self):
        User.objects.create_superuser(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')

        # Create a Excavation
        self.excavation = Excavation.objects.create(
            n_excavacion='001',
            latitud='-12.345',
            longitud='-12.345',
            altura='2089'
        )
        # Create a Room
        self.room = Room.objects.create(
            n_estancia='001',
            n_zona='1',
            n_sector='1',
            fase='A1',
            periodo='Siglo XVIII'
        )
        # Create a SedimentaryUE
        self.sedimentary_ue = SedimentaryUE.objects.create(
            excavacion=self.excavation,
            n_orden='001',
        )
        # Create a BuiltUE
        self.built_ue = BuiltUE.objects.create(
            excavacion=self.excavation,
            n_orden='002',
        )
        # Create a fact
        self.fact = Fact.objects.create(
            letra='MR',
            numero='001',
            estancia=self.room,
        )
        # Create a inclusion
        self.inclusion = Inclusion.objects.create(
            tipo='Cenizas',
            uesedimentaria=self.sedimentary_ue,
            frecuencia='Ausencia',
            grosor='< 2 cm',
        )
        # Create a photo
        self.photo = Photo.objects.create(
            numero='001',
            ue=self.sedimentary_ue,
            estancia=self.room,
        )
        # Create a SedimentaryMaterial
        self.sedimentary_material = SedimentaryMaterial.objects.create(
            nombre='Material 1'
        )
        # Create a BuiltMaterial
        self.built_material = BuiltMaterial.objects.create(
            nombre='Material 2'
        )

    def test_models_registered(self):
        response = self.client.get('/admin/myFindings/')
        self.assertContains(response, 'Estancias')
        self.assertContains(response, 'Excavaciones')
        self.assertContains(response, 'Fotografías')
        self.assertContains(response, 'Hechos')
        self.assertContains(response, 'Inclusiones')
        self.assertContains(response, 'Materiales construidos')
        self.assertContains(response, 'Materiales sedimentarios')
        self.assertContains(response, 'Unidades construidas')
        self.assertContains(response, 'Unidades sedimentarias')
    
    def test_room_readonly_fields(self):
        response = self.client.get('/admin/myFindings/room/' + str(self.room.id) + '/change/')
        self.assertContains(response, 'readonly', count=1)

    def test_fact_readonly_fields(self):
        response = self.client.get('/admin/myFindings/fact/' + str(self.fact.id) + '/change/')
        self.assertContains(response, 'readonly', count=2)

    def test_excavation_readonly_fields(self):
        response = self.client.get('/admin/myFindings/excavation/' + str(self.excavation.id) + '/change/')
        self.assertContains(response, 'readonly', count=1)

    def test_photo_readonly_fields(self):
        response = self.client.get('/admin/myFindings/photo/' + str(self.photo.id) + '/change/')
        self.assertContains(response, 'readonly', count=1)

    def test_sedimentary_ue_readonly_fields(self):
        response = self.client.get('/admin/myFindings/sedimentaryue/' + str(self.sedimentary_ue.id) + '/change/')
        self.assertContains(response, 'readonly', count=3)

    def test_built_ue_readonly_fields(self):
        response = self.client.get('/admin/myFindings/builtue/' + str(self.built_ue.id) + '/change/')
        self.assertContains(response, 'readonly', count=3)

    def test_sedimentary_material_readonly_fields(self):
        response = self.client.get('/admin/myFindings/sedimentarymaterial/' + str(self.sedimentary_material.nombre) + '/change/')
        self.assertContains(response, 'readonly', count=1)

    def test_built_material_readonly_fields(self):
        response = self.client.get('/admin/myFindings/builtmaterial/' + str(self.built_material.nombre) + '/change/')
        self.assertContains(response, 'readonly', count=1)

    def test_inclusion_readonly_fields(self):
        response = self.client.get('/admin/myFindings/inclusion/' + str(self.inclusion.id) + '/change/')
        self.assertContains(response, 'readonly', count=2)

    def test_sedimentary_ue_readonly_fields_creating(self):
        response = self.client.get('/admin/myFindings/sedimentaryue/add/')
        self.assertContains(response, 'readonly', count=1)

    def test_built_ue_readonly_fields_creating(self):
        response = self.client.get('/admin/myFindings/builtue/add/')
        self.assertContains(response, 'readonly', count=1)

    def test_room_readonly_fields_creating(self):
        response = self.client.get('/admin/myFindings/room/add/')
        self.assertContains(response, 'readonly', count=0)

    def test_fact_readonly_fields_creating(self):
        response = self.client.get('/admin/myFindings/fact/add/')
        self.assertContains(response, 'readonly', count=0)

    def test_excavation_readonly_fields_creating(self):
        response = self.client.get('/admin/myFindings/excavation/add/')
        self.assertContains(response, 'readonly', count=0)

    def test_photo_readonly_fields_creating(self):
        response = self.client.get('/admin/myFindings/photo/add/')
        self.assertContains(response, 'readonly', count=0)

    def test_builtmaterial_readonly_fields_creating(self):
        response = self.client.get('/admin/myFindings/builtmaterial/add/')
        self.assertContains(response, 'readonly', count=0)

    def test_sedimentarymaterial_readonly_fields_creating(self):
        response = self.client.get('/admin/myFindings/sedimentarymaterial/add/')
        self.assertContains(response, 'readonly', count=0)
        
    def test_inclusion_readonly_fields_creating(self):
        response = self.client.get('/admin/myFindings/inclusion/add/')
        self.assertContains(response, 'readonly', count=0)
        
    def test_room_list_display(self):
        response = self.client.get('/admin/myFindings/room/')
        self.assertContains(response, 'n_estancia')
        self.assertContains(response, 'n_zona')
        self.assertContains(response, 'n_sector')
        self.assertContains(response, 'fase')
        self.assertContains(response, 'periodo')

    def test_fact_list_display(self):
        response = self.client.get('/admin/myFindings/fact/')
        self.assertContains(response, 'letra')
        self.assertContains(response, 'numero')

    def test_excavation_list_display(self):
        response = self.client.get('/admin/myFindings/excavation/')
        self.assertContains(response, 'n_excavacion')
        self.assertContains(response, 'latitud')
        self.assertContains(response, 'longitud')
        self.assertContains(response, 'altura')

    def test_photo_list_display(self):
        response = self.client.get('/admin/myFindings/photo/')
        self.assertContains(response, 'numero')
        self.assertContains(response, 'ue')
        self.assertContains(response, 'estancia')

    def test_sedimentary_ue_list_display(self):
        response = self.client.get('/admin/myFindings/sedimentaryue/')
        self.assertContains(response, 'codigo')
        self.assertContains(response, 'excavacion')

    def test_built_ue_list_display(self):
        response = self.client.get('/admin/myFindings/builtue/')
        self.assertContains(response, 'codigo')
        self.assertContains(response, 'excavacion')

    def test_sedimentary_material_list_display(self):
        response = self.client.get('/admin/myFindings/sedimentarymaterial/')
        self.assertContains(response, 'nombre')

    def test_built_material_list_display(self):
        response = self.client.get('/admin/myFindings/builtmaterial/')
        self.assertContains(response, 'nombre')

    def test_inclusion_list_display(self):
        response = self.client.get('/admin/myFindings/inclusion/')
        self.assertContains(response, 'tipo')
        self.assertContains(response, 'uesedimentaria')
        self.assertContains(response, 'frecuencia')
        self.assertContains(response, 'grosor')
