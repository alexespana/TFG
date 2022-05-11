from collections import UserList
from django.db import models
import re
from django.core.exceptions import ValidationError

def validate_number(value):
    regex = r'^[0-9]{1,3}$'
    if not re.match(regex, value):
        raise ValidationError('Introduzca un formato de número positivo válido.')

    if(int(value) < 1 or int(value) > 999):
        raise ValidationError('El número debe ser mayor que 0.')

def validate_excavation(value):
    validate_number(value)
    excavation_number = value.zfill(3)

    if Excavation.objects.filter(n_excavacion=excavation_number).exists():
        raise ValidationError('Ya existe una excavación con este número.')

def validate_room(value):
    validate_number(value)
    room_number = value.zfill(3)

    if Room.objects.filter(n_estancia=room_number).exists():
        raise ValidationError('Ya existe una estancia con este número.')

def validate_ue(value):
    validate_number(value)
    ue_number = value.zfill(3)

    if UE.objects.filter(n_orden=ue_number).exists():
        raise ValidationError('Ya existe una unidad con ese número de orden para la misma excavación.')

FASE_CHOICES = [
    (('A: época contemporánea'), (
            ('A1','A1: Siglo XVIII'),
            ('A2','A2: Siglo XIX'),
            ('A3','A3: Siglo XX'),
        )
    ),
    (('B: época moderna'),(
            ('B1','B1: Siglo XV'),
            ('B2','B2: Siglo XVI'),
            ('B3','B3: Siglo XVII'),
        )
    ),
    (('C: época medieval'), (
            ('C1','C1: fase emiral'),
            ('C2','C2: fase califal'),
            ('C3','C3: fase taifas'),
            ('C4','C4: fase almorávide/almohade'),
            ('C5','C5: fase nazarí'),
        )
    ),
    (('D: época romana'), (
            ('D1','D1: época republicana'),
            ('D2','D2: Alto Imperio'),
            ('D3','D3: Bajo Imperio'),
            ('D4','D4: Antigüedad tardía'),
        )
    ),
    (('E: época ibérica'), (
            ('E1','E1: Protoibérico-orientalizante'),
            ('E2','E2: Ibérico antiguo'),
            ('E3','E3: Ibérico pleno'),
            ('E4','E4: Ibérico tardío o final'),
        )
    ),
    (('F: Edad del Bronce'), (
            ('F1','F1: Bronce Antiguo'),
            ('F2','F2: Bronce Pleno'),
            ('F3','F3: Bronce Tardío'),
            ('F4','F4: Bronce Final'),
        )
    ),
]

PERIODO_CHOICES = [
    ('Siglo XVIII','Contemporánea: Siglo XVIII'),
    ('Siglo XIX','Contemporánea: Siglo XIX'),
    ('Siglo XX','Contemporánea: Siglo XX'),
    ('Siglo XV','Moderna: Siglo XV'),
    ('Siglo XVI','Moderna: Siglo XVI'),
    ('Siglo XVII','Moderna: Siglo XVII'),
    ('Fase emiral','Medieval: emiral'),
    ('Fase califal','Medieval: califal'),
    ('Fase taifas','Medieval: taifas'),
    ('Fase invasiones almorávides y almohades','Medieval: almorávide/almohade'),
    ('Fase nazarí','Medieval: nazarí'),
    ('Fase republicana','Romana: época republicana'),
    ('Fase Altoimperial','Romana: Alto Imperio'),
    ('Fase Bajoimperial','Romana: Bajo Imperio'),
    ('Antigüedad tardía','Romana: Antigüedad tardía'),
    ('Protoibérico-orientalizante','Ibérica: Protoibérico'),
    ('Ibérico antiguo','Ibérica: Ibérico antiguo'),
    ('Ibérico pleno','Ibérica: Ibérico pleno'),
    ('Ibérico final','Ibérica: Ibérico tardío o final'),
    ('Bronce antiguo','Edad del Bronce: Antiguo'),
    ('Bronce pleno','Edad del Bronce: Pleno'),
    ('Bronce tardío','Edad del Bronce: Tardío'),
    ('Bronce final','Edad del Bronce: Final'),
]


# Create your models here.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ESTANCIA            ~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Room(models.Model):
    # 1, 2, 3, 4, etc
    n_estancia = models.CharField(max_length=3, verbose_name='Número de estancia', 
                                  help_text='Ej. 1, 2, 3, etc', validators=[validate_room], unique=True)
    n_zona = models.PositiveSmallIntegerField(verbose_name='Número de zona', blank=True, null=True)
    n_sector = models.PositiveSmallIntegerField(verbose_name='Número de sector', blank=True, null=True)
    observaciones = models.CharField(max_length=200, blank=True, null=True)
    croquis_planta = models.ImageField(verbose_name='Croquis de la planta', blank=True, null=True)
    n_planta = models.PositiveSmallIntegerField(verbose_name='Número de planta', blank=True, null=True)
    n_seccion = models.PositiveSmallIntegerField(verbose_name='Número de sección',blank=True, null=True)
    elevacion = models.PositiveSmallIntegerField(verbose_name='Número de elevación',blank=True, null=True)
    tpq = models.PositiveSmallIntegerField(verbose_name='Terminus Post Quem (TPQ)',blank=True, null=True)
    taq = models.PositiveSmallIntegerField(verbose_name='Terminus Ante Quem (TAQ)', blank=True, null=True)
    fase = models.CharField(max_length=2, choices=FASE_CHOICES, blank=True, null=True)
    periodo = models.CharField(max_length=100, choices=PERIODO_CHOICES, blank=True, null=True)
    autor = models.CharField(max_length=50, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.n_estancia = self.n_estancia.zfill(3)
        super(Room, self).save(*args, **kwargs)

    def __str__(self):
        return self.n_estancia

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# EXCAVACION          ~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Excavation(models.Model):
    # Ej. 001, 002, 003, etc
    n_excavacion = models.CharField(max_length=3, verbose_name='Número de excavación', help_text='Ej. 1, 2, 3, etc', 
                                    validators=[validate_excavation], unique=True)      
    latitud = models.FloatField(blank=True, null=True)
    longitud = models.FloatField(blank=True, null=True)
    altura = models.PositiveSmallIntegerField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.n_excavacion = self.n_excavacion.zfill(3)
        super(Excavation, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.n_excavacion)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# HECHO               ~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Fact(models.Model):
    LETRA_CHOICES = [
        ('MR','Muro'),
        ('SL','Suelo'),
        ('PO','Pozo'),
        ('FS','Fosa'),
        ('SI','Silo'),
        ('PR','Puerta'),
        ('CN','Canalización'),
        ('DP','Depósito'),
        ('TN','Tinaja'),
        ('ES','Sin identificación'),
    ]

    # Foreign keys
    estancia = models.ForeignKey(Room, on_delete=models.CASCADE, to_field='n_estancia', blank=True, null=True)

    # Unique key
    letra = models.CharField(max_length=2, choices=LETRA_CHOICES)
    numero = models.CharField(max_length=6, verbose_name='Número (UE que lo identifica)')    # Number of stratigrafic unit that identifies the fact

    fase = models.CharField(max_length=2, choices=FASE_CHOICES, blank=True, null=True)
    tpq = models.PositiveSmallIntegerField(verbose_name='Terminus Post Quem (TPQ)',blank=True, null=True)
    taq = models.PositiveSmallIntegerField(verbose_name='Terminus Ante Quem (TAQ)', blank=True, null=True)
    definicion = models.CharField(max_length=100, blank=True, null=True)
    comentarios = models.CharField(max_length=100, blank=True, null=True)
    sector = models.PositiveSmallIntegerField(verbose_name='Número de sector', blank=True, null=True)
    zona = models.PositiveSmallIntegerField(verbose_name='Número de zona', blank=True, null=True)
    año = models.PositiveSmallIntegerField(blank=True, null=True)
    estructura = models.PositiveSmallIntegerField(verbose_name='Número de estructura', blank=True, null=True) 
    croquis_plan = models.ImageField(verbose_name='Croquis del plan', blank=True, null=True)
    croquis_seccion = models.ImageField(verbose_name='Croquis de la sección', blank=True, null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['letra', 'numero'], name='fact_constraint')                                                  
        ]

    def __str__(self):
        return self.letra + self.numero


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# UE                  ~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class UE(models.Model):
    INTERPRETACION_CHOICES = [
        ('Ocupación','Ocupación'),
        ('Abandono','Abandono'),
        ('Construcción','Construcción'),
        ('Paleosuelo','Paleosuelo'),
        ('Reinstalación','Reinstalación'),
        ('Coluvión/Aluvión','Coluvión/Aluvión'),
        ('Destrucción','Destrucción'),
        ('Relleno','Relleno'),
        ('Otras','Otras'),
    ]

    PENDIENTE_CHOICES = [
        ('Norte','Norte'),
        ('Sur','Sur'),
        ('Este','Este'),
        ('Oeste','Oeste'),
        ('Noroeste','Noroeste'),
        ('Noreste','Noreste'),
        ('Suroeste','Suroeste'),
        ('Sureste','Sureste'),
    ]

    codigo = models.CharField(unique=True, max_length=6, blank=True)
    n_orden = models.CharField(max_length=3, verbose_name='Número de orden', 
                                help_text='Ej. 1, 2, 3, etc', validators=[validate_ue]) 

    # Foreign Keys
    hecho = models.ForeignKey(Fact, on_delete=models.CASCADE, blank=True, null=True)
    excavacion = models.ForeignKey(Excavation, on_delete=models.CASCADE, to_field='n_excavacion')

    plano_n = models.PositiveSmallIntegerField(verbose_name='Número de plano', blank=True, null=True)
    seccion_n = models.PositiveSmallIntegerField(verbose_name='Número de sección', blank=True, null=True)
    elevacion_n = models.PositiveSmallIntegerField(verbose_name='Número de elevación', blank=True, null=True)
    croquis_planta = models.ImageField(verbose_name='Croquis de la planta', blank=True, null=True)
    croquis_seccion = models.ImageField(verbose_name='Número de la sección', blank=True, null=True)
    tpq = models.PositiveSmallIntegerField(verbose_name='Terminus Post Quem (TPQ)',blank=True, null=True)
    taq = models.PositiveSmallIntegerField(verbose_name='Terminus Ante Quem (TAQ)', blank=True, null=True)
    fase = models.CharField(max_length=2, choices=FASE_CHOICES, blank=True, null=True)
    periodo = models.CharField(max_length=100, choices=PERIODO_CHOICES, blank=True, null=True)
    descripcion = models.TextField(max_length=200, blank=True, null=True)
    autor = models.CharField(max_length=30, blank=True, null=True)
    año = models.PositiveSmallIntegerField(blank=True, null=True)
    interpretacion = models.CharField(max_length=16, choices=INTERPRETACION_CHOICES, blank=True, null=True)    
    sector = models.PositiveSmallIntegerField(verbose_name='Número de sector', blank=True, null=True)          
    observaciones = models.TextField(max_length=200, blank=True, null=True)
    latitud = models.FloatField(blank=True, null=True)
    longitud = models.FloatField(blank=True, null=True)
    cota_superior_diff = models.FloatField(verbose_name='Cota superior (diferencia con punto cero)', blank=True, null=True)
    cota_inferior_diff = models.FloatField(verbose_name='Cota inferior (diferencia con punto cero)', blank=True, null=True)
    pendiente_superior = models.CharField(max_length=8, choices=PENDIENTE_CHOICES, blank=True, null=True)
    pendiente_inferior = models.CharField(max_length=8, choices=PENDIENTE_CHOICES,  blank=True, null=True)

    # Calculated fields
    cota_superior = models.FloatField(blank=True, null=True)
    cota_inferior = models.FloatField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.n_orden = self.n_orden.zfill(3)
        self.codigo = self.excavacion.n_excavacion + self.n_orden

        if(self.excavacion.altura and self.cota_superior_diff):
            self.cota_superior = self.excavacion.altura + self.cota_superior_diff
        if(self.excavacion.altura and self.cota_inferior_diff):
            self.cota_inferior = self.excavacion.altura + self.cota_inferior_diff
        super(UE, self).save(*args, **kwargs)

    def __str__(self):
        return self.codigo

class Photo(models.Model):
    numero = models.PositiveIntegerField(unique=True)
   
    # Foreign Keys
    ue = models.ForeignKey(UE, on_delete=models.CASCADE, verbose_name='UE (sedimentaria o construida)', blank=True, null=True)
    estancia = models.ForeignKey(Room, on_delete=models.CASCADE, blank=True, null=True)

    tipo = models.CharField(max_length=50, blank=True, null=True)
    fase = models.CharField(max_length=2, choices=FASE_CHOICES, blank=True, null=True)
    vista_desde = models.CharField(max_length=50, blank=True, null=True)
    dist_focal = models.PositiveSmallIntegerField(verbose_name='Distancia focal', blank=True, null=True)
    descripcion = models.TextField(max_length=200, blank=True, null=True)
    imagen = models.ImageField(blank=True, null=True)

    def __str__(self):
        return str(self.numero)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# MATERIALSEDIMENTARIA ~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class SedimentaryMaterial(models.Model):
    nombre = models.CharField(max_length=40, primary_key=True)

    def __str__(self):
        return self.nombre

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# MATERIALCONSTRUIDA   ~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class BuiltMaterial(models.Model):
    nombre = models.CharField(max_length=40, primary_key=True)

    def __str__(self):
        return self.nombre

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# UESEDIMENTARIA      ~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class SedimentaryUE(UE):
    ESTRUCTURA_CHOICES = [
        ('Compacta', 'Compacta'),
        ('Suelta', 'Suelta'),
        ('Homogénea', 'Homogénea'),
        ('Heterogénea', 'Heterogénea'),
    ]

    TEXTURA_CHOICES = [
        ('Arcilla','Arcilla'),
        ('Limo','Limo'),
        ('Arena','Arena'),
        ('Grava','Grava'),
        ('Cantos','Cantos'),
        ('Bloques','Bloques'),
        ('Cerámica','Cerámica'),
        ('Mortero','Mortero'),
    ]

    tipo_estructura = models.CharField(max_length=15, verbose_name='Tipo de estructura', choices=ESTRUCTURA_CHOICES, blank=True, null=True)
    tipo_textura = models.CharField(max_length=10, verbose_name='Tipo de textura', choices=TEXTURA_CHOICES, blank=True, null=True)
    materiales = models.ManyToManyField(SedimentaryMaterial, blank=True)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# UECONSTRUIDA        ~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class BuiltUE(UE):
    TIPO_CHOICES = [
        ('Positiva', 'Positiva'),
        ('Negativa', 'Negativa'),
    ]

    sistema_constructivo = models.CharField(max_length=50, blank=True, null=True)
    tipo = models.CharField(max_length=8, choices=TIPO_CHOICES, default='Positiva')
    materiales = models.ManyToManyField(BuiltMaterial, blank=True)
    n_estructura = models.PositiveSmallIntegerField(verbose_name='Número de estructura' , blank=True, null=True)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# INCLUSION           ~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Inclusion(models.Model):
    FRECUENCIA_CHOICES = [
        ('Ausencia', 'Ausencia'),
        ('Ocasional', 'Ocasional'),
        ('Medio', 'Medio'),
        ('Frecuente', 'Frecuente'),
    ]

    GROSOR_CHOICES = [
        ('< 2 cm', '< 2 cm'),
        ('2-6 cm', '2-6 cm'),
        ('6-12 cm', '6-12 cm'),
        ('> 12 cm', '> 12 cm'),
    ]

    TIPO_CHOICES = [
        ('Cenizas', 'Cenizas'),
        ('Carbones', 'Carbones'),
        ('Huesos', 'Huesos'),
        ('Adobe', 'Adobe'),
        ('Cañizo', 'Cañizo'),
        ('Tejas', 'Tejas'),
        ('Bloques', 'Bloques'),
        ('Cal', 'Cal'),
        ('Mortero', 'Mortero'),
        ('Enlucido', 'Enlucido'),
    ]
    
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)

    # Foreign Keys
    uesedimentaria = models.ForeignKey(SedimentaryUE, on_delete=models.CASCADE, verbose_name='UE sedimentaria')

    frecuencia = models.CharField(max_length=10, choices=FRECUENCIA_CHOICES, blank=True, null=True)
    grosor = models.CharField(max_length=10, choices=GROSOR_CHOICES, blank=True, null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['tipo', 'uesedimentaria'], name='inclusion_constraint')                                                  
        ]

    def __str__(self):
        return self.tipo + ' - ' + self.uesedimentaria.codigo
