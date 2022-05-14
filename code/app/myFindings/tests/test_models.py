from django.test import TestCase
from myFindings.models import UE, Excavation, Room, validate_number
from django.core.exceptions import ValidationError

class TestModels(TestCase):

    def setUp(self):
        self.excavation = Excavation.objects.create(
            n_excavacion = '001',
            latitud = 1.0,
            longitud = 1.0,
            altura = 1200,
        )
        self.ue = UE.objects.create(
            n_orden = '002',
            excavacion = self.excavation,
            cota_superior_diff = 1.3,
            cota_inferior_diff = -1.2,
        )

    def test_excavation_str(self):
        self.assertEqual(str(self.excavation.n_excavacion), '001')

    def test_room_str(self):
        room = Room.objects.create(
            n_estancia = '001'
        )
        self.assertEqual(str(room), '001')

    def test_ue_code(self):
        self.assertEqual(self.ue.codigo, '001002')

    def test_upper_limit_correct(self):
        self.assertEqual(self.ue.cota_superior, 1201.3)

    def test_lower_limit_correct(self):
        self.assertEqual(self.ue.cota_inferior, 1198.8)

class TestValidators(TestCase):
    
    def test_validate_number_too_long(self):
        
        # It raise an ValidationError, check the message
        with self.assertRaises(ValidationError) as context:
            validate_number('123456789')
        self.assertEqual(context.exception.message, 'El número debe tener 3 dígitos.')

    def test_validate_number_too_short(self):
            
        # It raise an ValidationError, check the message
        with self.assertRaises(ValidationError) as context:
            validate_number('12')
        self.assertEqual(context.exception.message, 'El número debe tener 3 dígitos.')

    def test_validate_number_with_letters(self):
                
        # It raise an ValidationError, check the message
        with self.assertRaises(ValidationError) as context:
            validate_number('12a')
        self.assertEqual(context.exception.message, 'Introduzca un formato de número positivo válido.')


    def test_validate_number_with_negative_number(self):

        # It raise an ValidationError, check the message
        with self.assertRaises(ValidationError) as context:
            validate_number('-12')
        self.assertEqual(context.exception.message, 'Introduzca un formato de número positivo válido.')

    def test_validate_number_not_zero(self):
            
        # It raise an ValidationError, check the message
        with self.assertRaises(ValidationError) as context:
            validate_number('000')
        self.assertEqual(context.exception.message, 'El número debe ser mayor que 0.')