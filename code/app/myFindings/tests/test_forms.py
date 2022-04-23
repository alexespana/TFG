from django.test import TestCase
from myFindings.models import Estancia, Excavacion, Hecho, UESedimentaria

from myFindings.forms import ExcavationForm, FactForm, RoomForm, PhotoForm, \
    SedimentaryUEForm, BuiltUEForm, SedimentaryMaterialForm, BuiltMaterialForm, \
    InclusionForm, CustomUserCreationForm

class TestForms(TestCase):

    def setUp(self):
        self.excavation = Excavacion.objects.create(
            n_excavacion = 1
        )
        self.room = Estancia.objects.create(
            n_estancia = 'ES001'
        )
        self.fact = Hecho.objects.create(
            estancia = self.room,
            letra = 'SI',
            numero = '123',
        )
        self.sedimentaryue = UESedimentaria.objects.create(
            codigo = '000001',
            excavacion = self.excavation
        )

    def test_excavation_form_valid_data(self):
        form = ExcavationForm(data={
            'n_excavacion': 2,
            'latitud': 1.0,
            'longitud': 1.0,
            'altura': 1200,
        })

        self.assertTrue(form.is_valid())

    def test_excavation_form_invalid_data(self):
        form = ExcavationForm(data={})

        self.assertFalse(form.is_valid())

    def test_fact_form_valid_data(self):
        form = FactForm(data={
            'estancia': self.room.pk,
            'letra': 'SL',
            'numero': '123',
            'fase': 'A1',
            'tpq': 1,
            'taq': 2,
            'definicion': 'Definition',
            'comentarios': 'Comments',
            'sector': 12,
            'zona': 43,
            'año': 2021,
            'estructura': 3,
            'croquis_plan': '',
            'croquis_seccion': ''
        })

        self.assertTrue(form.is_valid())

    def test_fact_form_invalid_data(self):
        form = FactForm(data={})

        self.assertFalse(form.is_valid())

    def test_room_form_valid_data(self):
        form = RoomForm(data={
            'n_estancia': 'ES002',
            'n_zona': 1,
            'n_sector': 1,
            'observaciones': 'Observations',
            'n_planta': 1,
            'n_seccion': 1,
            'elevacion': 1,
            'tpq': 1,
            'taq': 2,
            'fase': 'A1',
            'periodo': 'Siglo XVIII',
            'author': 'me',
        })

        self.assertTrue(form.is_valid())

    def test_room_form_invalid_data(self):
        form = RoomForm(data={})

        self.assertFalse(form.is_valid())

    def test_photo_form_valid_data(self):
        form = PhotoForm(data={
            'numero': 23,
            'tipo': 'Foto',
            'fase': 'A1',
            'vista_desde': 'Norte',
            'dist_focal': 1,
            'descripcion': 'Description',
            'estancia': self.room.pk,
            'ue': self.sedimentaryue.pk,
        })

        self.assertTrue(form.is_valid())

    def test_photo_form_invalid_data(self):
        form = PhotoForm(data={})

        self.assertFalse(form.is_valid())

    def test_sedimentarymaterial_form_valid_data(self):
        form = SedimentaryMaterialForm(data={
            'nombre': 'Sedimentary Material',
        })

        self.assertTrue(form.is_valid())

    def test_sedimentarymaterial_form_invalid_data(self):
        form = SedimentaryMaterialForm(data={})

        self.assertFalse(form.is_valid())

    def test_builtmaterial_form_valid_data(self):
        form = BuiltMaterialForm(data={
            'nombre': 'Built Material',
        })

        self.assertTrue(form.is_valid())

    def test_builtmaterial_form_invalid_data(self):
        form = BuiltMaterialForm(data={})

        self.assertFalse(form.is_valid())

    def test_inclusion_form_valid_data(self):
        form = InclusionForm(data={
            'tipo': 'Cenizas',
            'uesedimentaria': self.sedimentaryue.pk,
            'frecuencia': 'Ausencia',
            'grosor': '< 2 cm',
        })

        self.assertTrue(form.is_valid())

    def test_inclusion_form_invalid_data(self):
        form = InclusionForm(data={})

        self.assertFalse(form.is_valid())

    def test_sedimentaryue_form_valid_data(self):
        form = SedimentaryUEForm(data={
            'codigo': '000002',
            'hecho': self.fact.pk,
            'excavacion': self.excavation.n_excavacion,
            'plano_n': 1,
            'seccion_n': 1,
            'elevacion_n': 1,
            'tpq': 1,
            'taq': 2,
            'fase': 'A1',
            'periodo': 'Siglo XVIII',
            'descripcion': 'Description',
            'autor': 'me',
            'año': 2021,
            'interpretacion': 'Ocupación',
            'sector': 12,
            'observaciones': 'Observations',
            'latitud': 1.0,
            'longitud': 1.0,
            'cota_superior_diff': -1,
            'cota_inferior_diff': -1,
            'pendiente_superior': 'Norte',
            'pendiente_inferior': 'Noroeste',
            'tipo_estructura': 'Compacta',
            'tipo_textura': 'Arcilla',
            'materiales': ['Muestras', 'Metal'],
        })

        self.assertTrue(form.is_valid())

    def test_sedimentaryue_form_invalid_data(self):
        form = SedimentaryUEForm(data={})

        self.assertFalse(form.is_valid())

    def test_builtue_form_valid_data(self):
        form = BuiltUEForm(data={
            'codigo': '000002',
            'hecho': self.fact.pk,
            'excavacion': self.excavation.n_excavacion,
            'plano_n': 1,
            'seccion_n': 1,
            'elevacion_n': 1,
            'tpq': 1,
            'taq': 2,
            'fase': 'A1',
            'periodo': 'Siglo XVIII',
            'descripcion': 'Description',
            'autor': 'me',
            'año': 2021,
            'interpretacion': 'Ocupación',
            'sector': 12,
            'observaciones': 'Observations',
            'latitud': 1.0,
            'longitud': 1.0,
            'cota_superior_diff': -1,
            'cota_inferior_diff': -1,
            'pendiente_superior': 'Norte',
            'pendiente_inferior': 'Noroeste',
            'sistema_constructivo': 'Compacta',
            'tipo': 'Positiva',
            'materiales': ['Piedra', 'Cal'],
            'n_estructura': 1,
        })

        self.assertTrue(form.is_valid())

    def test_builtue_form_invalid_data(self):
        form = BuiltUEForm(data={})

        self.assertFalse(form.is_valid())

    def test_customusercreation_form_invalid_data(self):
        form = CustomUserCreationForm(data={})

        self.assertFalse(form.is_valid())