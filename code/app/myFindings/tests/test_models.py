from django.test import TestCase
from myFindings.models import UE, Excavation, Room
class TestModels(TestCase):

    def setUp(self):
        self.excavation = Excavation.objects.create(
            n_excavacion = '1',
            latitud = 1.0,
            longitud = 1.0,
            altura = 1200,
        )
        self.ue = UE.objects.create(
            n_orden = '2',
            excavacion = self.excavation,
            cota_superior_diff = 1.3,
            cota_inferior_diff = -1.2,
        )

    def test_excavation_str(self):
        self.assertEqual(str(self.excavation.n_excavacion), '001')

    def test_room_str(self):
        room = Room.objects.create(
            n_estancia = '1'
        )
        self.assertEqual(str(room), '001')

    def test_ue_code(self):
        self.assertEqual(self.ue.codigo, '001002')

    def test_upper_limit_correct(self):
        self.assertEqual(self.ue.cota_superior, 1201.3)

    def test_lower_limit_correct(self):
        self.assertEqual(self.ue.cota_inferior, 1198.8)
